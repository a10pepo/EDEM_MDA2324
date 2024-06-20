""" 
Script: Streaming Data Generator

Description: The generator will publish new records into a PubSub Topic.

EDEM. Master Data Analytics 2023/2024
Professor: Javi Briones
"""

""" Import libraries """

from google.cloud import pubsub_v1
import threading
import argparse
import logging
import secrets
import random
import string
import json
import time

#Input arguments
parser = argparse.ArgumentParser(description=('Streaming Data Generator'))

parser.add_argument(
                '--project_id',
                required=True,
                help='GCP cloud project name.')
parser.add_argument(
                '--topic_name',
                required=True,
                help='PubSub topic name.')

args, opts = parser.parse_known_args()

""" Helpful Code """

class PubSubMessages:

    """ Publish Messages in our PubSub Topic """

    def __init__(self, project_id: str, topic_name: str):
        self.publisher = pubsub_v1.PublisherClient()
        self.project_id = project_id
        self.topic_name = topic_name

    def publishMessages(self, message: str):
        json_str = json.dumps(message)
        topic_path = self.publisher.topic_path(self.project_id, self.topic_name)
        self.publisher.publish(topic_path, json_str.encode("utf-8"))

    def __exit__(self):
        self.publisher.transport.close()
        logging.info("PubSub Client closed.")

def run_generator(project_id: str, topic_name: str):

    """ Method to simulate streaming data.
    Params:
        project_id (str): Google Cloud Project ID.
        topic_name (str): Google Pub Sub Topic Name.
    Returns:
        -
    """

    pubsub_class = PubSubMessages(project_id, topic_name)

    # Simulate Vehicle ID

    while True:

        temp: int = random.randint(1,20)

        logging.info("New temperature has been generated: %s", temp)

        pubsub_class.publishMessages({"temp": temp})

        time.sleep(10)

if __name__ == "__main__":
    
    # Set Logs
    logging.getLogger().setLevel(logging.INFO)
    
    # Run Generator
    run_generator(
        args.project_id, args.topic_name)