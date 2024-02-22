import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor_sensor_get(sensor):  # noqa: E501
    """Obtiene la última medida de temperatura de un sensor.

     # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Measure
    """
    return 'do some magic!'
