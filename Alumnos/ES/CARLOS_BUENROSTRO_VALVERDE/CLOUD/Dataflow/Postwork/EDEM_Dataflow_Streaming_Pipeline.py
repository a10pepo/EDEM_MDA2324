""" 
Script: Dataflow Streaming Pipeline
Description: This script will be responsible for processing 
messages ingested by our messaging queue from the device and:
    1. Calculate the average speed per vehicle in the section.
    2. Invoke the Vision AI model if the speed exceeds the allowed limit in the section.
    3. Finally, all the information will be sent to another topic for further analysis.
EDEM. Master Data Analytics 2024
Professor: Javi Briones
"""

""" Import libraries """

# Import Beam Libraries

import apache_beam as beam
from apache_beam.runners import DataflowRunner
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
from apache_beam.metrics import Metrics

# Dataflow ML
from apache_beam.ml.inference.base import ModelHandler
from apache_beam.ml.inference.base import RunInference

# Import GCP Libraries
from google.cloud.vision_v1.types import Feature
from google.cloud import vision

# Import Common Libraries
import argparse
import requests
import logging
import json
import re
import io

beam.options.pipeline_options.PipelineOptions.allow_non_parallel_instruction_output = True
DataflowRunner.__test__ = False


""" Helpful functions """
def ParsePubSubMessage(message):

    # Decode PubSub message in order to deal with
    pubsub_message = message.decode('utf-8')

    # Convert string decoded in JSON format
    msg = json.loads(pubsub_message)

    logging.info("New message in PubSub: %s", msg)

    # Return function
    return msg

def getVehicleImage(item,api_url):

    import requests
    import io

    # API call to simulate a photo captured by the radar
    image_service = requests.get(api_url)
    image_url = json.loads(image_service.content.decode('utf-8'))['image_url']

    #Read image from URL
    image_response = requests.get(image_url)
    image_bytes = io.BytesIO(image_response.content).read()

    #Append image_url to the payload
    item ['image_url'] = image_url

    logging.info(image_url)

    return item, image_bytes

def format_coordinates(element):
    # Asegúrate de que el campo 'coordinates' es una lista o tupla con dos elementos: [longitud, latitud]
    if 'coordinates' in element and isinstance(element['coordinates'], (list, tuple) ) and len(element['coordinates']) == 2:
        longitude, latitude = element['coordinates']
        # Convertir a formato WKT
        element['coordinates'] = f'POINT({longitude} {latitude})'
    return element


class CloudVisionModelHandler(ModelHandler):

    def load_model(self):

        """Initiate the Google Vision API client."""

        from google.cloud import vision
        from google.cloud.vision_v1.types import Feature

        client = vision.ImageAnnotatorClient()
        return client

    def run_inference(self, batch, model, inference):

        from google.cloud import vision
        from google.cloud.vision_v1.types import Feature

        from apache_beam.runners import DataflowRunner

        feature = Feature()
        feature.type_ = Feature.Type.TEXT_DETECTION

        images = [vision.Image(content=image_bytes) for (item, image_bytes) in batch]
        item_list = [item for (item, image_bytes) in batch]

        image_requests = [vision.AnnotateImageRequest(image=image, features=[feature]) for image in images]
        batch_image_request = vision.BatchAnnotateImagesRequest(requests=image_requests)

        model_responses = model.batch_annotate_images(request=batch_image_request).responses

        response = model_responses[0].text_annotations
        output_dict = item_list[0]

        license_plate = [text.description for text in response if text.description.isalnum() and not (text.description.isalpha() or text.description.isdigit())]

        yield output_dict, license_plate

class OutputFormatDoFn(beam.DoFn):

    def process(self, element):

        output_dict, license_plate = element

        if len(license_plate) > 0 :


            output_dict['license_plate'] = license_plate[0] if len(license_plate) > 0 else "not recognized"

            yield output_dict

        else:

            output_dict['license_plate'] = "no texts found"
            yield output_dict


# DoFn

class getVehicleDoFn(beam.DoFn):

    def process(self, element):

        # Get vehicle_id from input payload
        yield element['vehicle_id'], element

class avgSpeedDoFn(beam.DoFn):

    def __init__(self,radar_id):

        self.countFinedVehicles = Metrics.counter('main', 'Count of fined vehicles.')
        self.countNonFinedVehicles = Metrics.counter('main', 'Count of non-fined vehicles.')
        self.radar_id = radar_id

    def process(self, element):

        import apache_beam as beam

        key, payload = element

        avg_speed = sum(e["speed"] for e in payload)/len(payload)

        output_dict = {
            "radar_id": self.radar_id,
            "vehicle_id": key,
            "avg_speed": avg_speed,
            "coordinates": payload[-1]['location']
        }

        if avg_speed > 40:

            output_dict['is_Ticketed'] = True

            #Metrics
            # self.countFinedVehicles.inc()

            yield beam.pvalue.TaggedOutput("fined_vehicles", output_dict)

        else:

            output_dict['is_Ticketed'] = False
            output_dict['license_plate'] = None

            #Metrics
            # self.countNonFinedVehicles.inc()

            yield beam.pvalue.TaggedOutput("non_fined_vehicles", output_dict)


""" Dataflow Process """

def run():

    """ Input Arguments"""
    parser = argparse.ArgumentParser(description=('Arguments for the Dataflow Streaming Pipeline.'))

    parser.add_argument(
                '--project_id',
                required=True,
                help='GCP cloud project name.')

    parser.add_argument(
                '--input_subscription',
                required=True,
                help='PubSub subscription from which we will read data from the generator.')

    parser.add_argument(
                '--output_topic',
                required=False,
                help='PubSub Topic which will be the sink for our data.')

    parser.add_argument(
                '--radar_id',
                required=True,
                help="Radar ID corresponding to the student's name.")

    parser.add_argument(
                '--cars_api',
                required=False,
                default='https://europe-west1-long-flame-410209.cloudfunctions.net/car-license-plates-api',
                help="API for retrieving vehicle images.")

    args, pipeline_opts = parser.parse_known_args()


    """ Apache Beam Pipeline """

    # Pipeline Options
    options = PipelineOptions(pipeline_opts,
        save_main_session=True, streaming=True, project=args.project_id)

    # Pipeline

    with beam.Pipeline(argv=pipeline_opts,options=options) as p:

        """ Part 01: Read data from PubSub. """

        data = (
            p
                | "Read From PubSub" >> beam.io.ReadFromPubSub(subscription=args.input_subscription)
                | "Parse JSON messages" >> beam.Map(ParsePubSubMessage)
        )

        """ Part 02: Get the aggregated data of the vehicle within the section. """

        processed_data = (

            data 
                | "Extract vehicle id data" >> beam.ParDo(getVehicleDoFn())
                | "User-window based on each vehicle" >> beam.WindowInto(window.Sessions(15),timestamp_combiner=window.TimestampCombiner.OUTPUT_AT_EOW)
                | "Group by ID" >> beam.GroupByKey()
                | "Avg Speed" >> beam.ParDo(avgSpeedDoFn(radar_id=args.radar_id)).with_outputs('fined_vehicles', 'non_fined_vehicles')

        )

        (
            processed_data.fined_vehicles
                | "Capture Vehicle image" >> beam.Map(getVehicleImage, api_url=args.cars_api)
                | "Model Inference" >> RunInference(model_handler=CloudVisionModelHandler())
                | "Output Format" >> beam.ParDo(OutputFormatDoFn())
                | "Format Coordinates" >> beam.Map(format_coordinates)           
                | "Write to BigQuery" >> beam.io.WriteToBigQuery(
                    table = "dataflow-cabuva:dataflow_cabuva.fined-vehicles", # Required Format: PROJECT_ID:DATASET.TABLE
                    schema='radar_id:STRING,vehicle_id:STRING,avg_speed:FLOAT,coordinates:STRING,is_Ticketed:BOOLEAN,image_url:STRING,license_plate:STRING',  # Required Format: field:TYPE
                    create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

        (
            processed_data.non_fined_vehicles 
                | "Encode non_fined_vehicles to Bytes" >> beam.Map(lambda x: json.dumps(x).encode("utf-8"))
                | "Write non_fined_vehicles to PubSub" >> beam.io.WriteToPubSub(topic=args.output_topic)
        )


if __name__ == '__main__':

    # Set Logs
    logging.getLogger().setLevel(logging.INFO)

    logging.info("The process started")

    # Run Process
    run()