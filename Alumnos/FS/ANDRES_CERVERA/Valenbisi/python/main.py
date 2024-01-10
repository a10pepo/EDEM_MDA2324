import requests
from pymongo import MongoClient
import pandas as pd
import time
import socket

username = "admin"
password = "admin01"
database_name = "estaciones_valenbisi"
collection_name = "estaciones"

# Esperar hasta que MongoDB esté listo
max_retries = 30
retry_interval = 5  # Aumentado el intervalo a 5 segundos

def is_mongo_available():
    host = "mongodb"
    port = 27017
    try:
        sock = socket.create_connection((host, port), timeout=1)
        sock.close()
        return True
    except Exception as e:
        return False

for _ in range(max_retries):
    if is_mongo_available():
        break
    print(f"MongoDB no está disponible. Reintentando en {retry_interval} segundos...")
    time.sleep(retry_interval)
else:
    print("No se pudo conectar a MongoDB después de varios intentos. Saliendo.")
    exit(1)

client = MongoClient("mongodb://admin:admin01@mongodb:27017/?authSource=admin")
db = client[database_name]
collection = db[collection_name]

result = collection.delete_many({})  # Borrar base de datos

URL = "https://valencia.opendatasoft.com/api/explore/v2.1/catalog/datasets/valenbisi-disponibilitat-valenbisi-dsiponibilidad/records?limit=100"

respuesta = requests.get(url=URL)
estado = respuesta.status_code
datos = respuesta.json()

if estado == 200:
    total_count = datos['total_count']
    print(f'Total de estaciones: {total_count}')

    # Ordenar datos por id_estacion ascendente
    sorted_data = sorted(datos["results"], key=lambda x: x["number"])

    data_list = []

    for estacion in sorted_data:
        id_estacion = estacion["number"]
        direccion = estacion["address"]
        fecha = estacion["updated_at"]
        bicis_disponibles = estacion["available"]
        huecos_libres = estacion["free"]

        print(f'Estación: {id_estacion}, Dirección: {direccion}, Bicis Disponibles: {bicis_disponibles}, Huecos Libres: {huecos_libres}, Fecha: {fecha}')

        # Insertar datos en la colección 'estaciones'
        data = {
            "id_estacion": id_estacion,
            "direccion": direccion,
            "bicis_disponibles": bicis_disponibles,
            "huecos_libres": huecos_libres,
            "fecha": fecha
        }

        # Utilizar update_one para insertar o actualizar
        collection.update_one(
            {"_id": id_estacion},
            {"$set": data},
            upsert=True
        )

else:
    print(f"Error: {estado}")