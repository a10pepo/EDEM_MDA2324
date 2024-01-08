import requests
import json

# URL del servidor KSQL
ksql_url = "http://localhost:8088"  # Asegúrate de cambiar esto por la URL correcta de tu servidor KSQL

# Headers para la solicitud
headers = {
    "Content-Type": "application/vnd.ksql.v1+json",
    "Accept": "application/vnd.ksql.v1+json"
}

# Función para enviar comandos KSQL
def send_ksql_command(ksql_command):
    response = requests.post(f"{ksql_url}/ksql", headers=headers, data=json.dumps(ksql_command))
    return response

# Obtener la lista de queries
response = send_ksql_command({"ksql": "SHOW QUERIES;"})
if response.status_code == 200:
    queries = response.json()[0]['queries']
    for query in queries:
        query_id = query['id']
        # Filtrar y detener las queries no internas
        if not query_id.startswith("_"):  # Asumiendo que las queries internas tienen un prefijo específico
            stop_command = {"ksql": f"TERMINATE {query_id};"}
            stop_response = send_ksql_command(stop_command)
            if stop_response.status_code == 200:
                print(f"Query {query_id} detenida con éxito.")
            else:
                print(f"No se pudo detener la query {query_id}: {stop_response.text}")
else:
    print("Error al obtener la lista de queries")
    print(response.text)
