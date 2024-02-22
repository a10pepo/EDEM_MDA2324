from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/getLastMeassureBySensor/<string:sensor>')
class SensorResource(Resource):
    def get(self, sensor):
        # Lógica para obtener la última medida por el sensor proporcionado
        # Puedes acceder al valor de 'sensor' usando la variable del mismo nombre
        # Ejemplo: sensor_id = sensor
        return {'message': 'Lógica para obtener la última medida por el sensor proporcionado'}

if __name__ == '__main__':
    app.run(debug=True)
