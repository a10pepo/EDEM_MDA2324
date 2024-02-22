from flask import Flask, jsonify
app = Flask(__name__)

# Datos ficticios de medidas de sensores
sensor_data = {
    "sensor001": [25.5, 26.0, 25.8, 25.7],
    "sensor002": [30.0, 30.2, 29.9, 30.1],
}

@app.route('/getLastMeassureBySensor/<sensor>', methods=['GET'])
def get_last_measure_by_sensor(sensor):
    if sensor in sensor_data:
        measurements = sensor_data[sensor]
        if measurements:
            last_measure = measurements[-1]  # Obtiene la última medida de la lista
            response = {
                'sensor': sensor,
                'last_measure': last_measure
            }
            return jsonify(response), 200
        else:
            return "No se encontraron medidas para el sensor", 400
    else:
        return "Sensor no encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)
