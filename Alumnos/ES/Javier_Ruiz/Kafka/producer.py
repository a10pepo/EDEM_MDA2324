from flask import Flask, jsonify
import requests
from kafka.producer import KafkaProducer
import json
import time

#API-get a AEMET + Envio a kafka topic
# Configuraciones
AEMET_API_KEY = 'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqYXZpZXJ1aXppbXBvcnRAZ21haWwuY29tIiwianRpIjoiNjdlNWFkNTEtNGU5Ni00OTBmLTgxOTktYTVhMTIzZTg5NGZhIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3MDcyMDc5NjAsInVzZXJJZCI6IjY3ZTVhZDUxLTRlOTYtNDkwZi04MTk5LWE1YTEyM2U4OTRmYSIsInJvbGUiOiIifQ.-Qa3SBTpCHiLGvQvc5d4eVNw8D9OR2fHNoqhVu_G1kk'
KAFKA_BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'topic_tiempo'

WEATHER_DATA_LIMIT = 200

# Instancia flask
app = Flask(__name__)


@app.route('/get_weather', methods=['GET'])
def get_weather_data():
    try:
        url = f'https://opendata.aemet.es/opendata/api/observacion/convencional/todas/?api_key={AEMET_API_KEY}'
        response = requests.get(url)
        data = response.json() # devuelve el siguiente json{'descripcion': 'exito', 'estado': 200, 'datos': 'url1', 'metadatos': 'url2'} , nos interesa la url1

        # Lista, ahora sí, con la informacion relevante
        weather_data = parse_weather_data(data)

        #Envio a un topic de KAFKA
        senddata(weather_data)

        return jsonify({'status': 'success', 'weather_data': weather_data}), 200

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

def parse_weather_data(data, limit=WEATHER_DATA_LIMIT):
    # Obtener la URL de los datos meteorológicos: url1 
    datos_url = data.get('datos')

    if not datos_url:
        raise Exception('La respuesta de la API de AEMET no incluye la URL de datos')

    # Realizo otra solicitud, esta vez a la URL de datos
    datos_response = requests.get(datos_url)
    weather_data_list = datos_response.json()

    # Me quedo con la informacion relevante
    parsed_data_list = []
    for i, entry in enumerate(weather_data_list):
        parsed_data = {
            "id": entry.get("idema"),
            "location": entry.get("ubi"),
            "timestamp": entry.get("fint"),
            "temperature": entry.get("ta"),
            "precipitation": entry.get("prec"),
            "humidity": entry.get("hr"),
            "wind_speed": entry.get("vv")
        }
        parsed_data_list.append(parsed_data)

        if i + 1 == limit:
            break

    return parsed_data_list



# ENVIO KAFKA

# Creo instancia de KafkaProducer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def senddata(weather_data):
    try:
        for entry in weather_data:
            producer.send(KAFKA_TOPIC, value=entry)
            print(f"Sending to Kafka: {entry}")
            time.sleep(2)
    finally:
        producer.close()



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
