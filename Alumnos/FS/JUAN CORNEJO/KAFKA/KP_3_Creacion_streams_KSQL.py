import requests
import json

def creacion_streams():
    ksql_url = "http://ksql-server:8088/ksql"
    headers = {
        "Content-Type": "application/vnd.ksql.v1+json",
        "Accept": "application/vnd.ksql.v1+json"
    }
    def send_ksql_command(command):
        payload = {"ksql": command, "streamsProperties": {}}
        response = requests.post(ksql_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Command '{command}' executed successfully.")
            print(response.json())
        else:
            print(f"Error executing command '{command}'")
            print(response.text)
    commands = [
        "CREATE STREAM emergencias_stream (tipo_emergencia VARCHAR, grado VARCHAR, cuerpo_necesario VARCHAR, localizacion VARCHAR, fecha VARCHAR, requiere_medico VARCHAR, contacto VARCHAR) WITH (KAFKA_TOPIC='T1_Recepcion_avisos', VALUE_FORMAT='JSON');",
        "CREATE STREAM Redireccion_Urgencias WITH (KAFKA_TOPIC='T2_Centro_112', VALUE_FORMAT='JSON') AS SELECT * FROM emergencias_stream WHERE grado='Urgencia extrema' OR grado='Urgente';",
        "CREATE STREAM Redireccion_No_Urgencias WITH (KAFKA_TOPIC='T3_No_Urgencias', VALUE_FORMAT='JSON') AS SELECT * FROM emergencias_stream WHERE grado<>'Urgencia extrema' AND grado<>'Urgente';",
        "CREATE STREAM Redireccion_Centro_Mando WITH (KAFKA_TOPIC='T2.2_Centro_de_mando', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_Urgencias WHERE requiere_medico='No';",
        "CREATE STREAM Redireccion_Medicos WITH (KAFKA_TOPIC='T3.1_Medicos', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE requiere_medico='Si' OR cuerpo_necesario ='Medicos';",
        "CREATE STREAM Redireccion_Bomberos WITH (KAFKA_TOPIC='T3.2_Bomberos', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE cuerpo_necesario ='Bomberos';",
        "CREATE STREAM Redireccion_Forestales WITH (KAFKA_TOPIC='T3.3_Forestales', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE cuerpo_necesario ='Forestales';",
        "CREATE STREAM Redireccion_Guardia_Costera WITH (KAFKA_TOPIC='T3.4_Guardia_Costera', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE cuerpo_necesario ='Guardia Costera';",
        "CREATE STREAM Redireccion_Policia WITH (KAFKA_TOPIC='T3.5_Policia', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE cuerpo_necesario ='Policia';",
        "CREATE STREAM Redireccion_Servicios_de_emergencia WITH (KAFKA_TOPIC='T3.6_Servicios_de_emergencia', VALUE_FORMAT='JSON') AS SELECT * FROM Redireccion_No_Urgencias WHERE cuerpo_necesario ='Servicios de emergencia';",
    ]
    for command in commands:
        send_ksql_command(command)

