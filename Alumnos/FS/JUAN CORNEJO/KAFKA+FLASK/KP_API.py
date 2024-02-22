from flask import Flask, jsonify, request, abort
from datetime import datetime
from KP_1_Definicion_clase import emergencia
import random

def levantar_api():
    app = Flask(__name__)

    @app.route('/generar_registros_emergencias/112', methods=['GET'])
    def generar_registros_emergencias():
        nueva_emergencia = emergencia()
        response = {
            "tipo_emergencia": nueva_emergencia.tipo_emergencia,
            "cuerpo_necesario": nueva_emergencia.cuerpo_necesario,
            "grado": nueva_emergencia.grado,
            "localizacion": nueva_emergencia.localizacion,
            "fecha": nueva_emergencia.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            "requiere_medico": nueva_emergencia.requiere_medico,
            "contacto": nueva_emergencia.contacto
        }
        return jsonify(response)

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
        print("API de emergencias levantada correctamente en http://0.0.0.0:5000")
levantar_api()