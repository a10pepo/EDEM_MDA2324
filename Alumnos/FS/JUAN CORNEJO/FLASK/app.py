from flask import Flask, jsonify, request, abort
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/getLastMeasureBySensor/<string:sensor>', methods=['GET'])
def get_last_measure(sensor):
    #Limitad el sensor a 100 para forzar error según pide el ejercicio.
    try:
        sensor_id = int(sensor)
        if sensor_id > 100:
            abort(400, description="Sensor no puede ser superior a 100")
    except ValueError:
        abort(404, description="ID suministrado inválido")

    last_temperature = round(random.uniform(-20, 50), 2)
    fecha_aleatoria_medicion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = {
        "code": sensor,
        "fechamuestreo": fecha_aleatoria_medicion,
        "unidad": "°C",
        "medicion": last_temperature
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)