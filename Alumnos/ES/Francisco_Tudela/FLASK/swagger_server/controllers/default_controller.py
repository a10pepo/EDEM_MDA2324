import connexion
import six

from swagger_server.models.measure import Measure  # noqa: E501
from swagger_server import util


def get_last_measure_by_sensor_sensor_get(sensor):  # noqa: E501
    """Get the last temperature measurement by sensor

    Retrieves the latest temperature measurement for a specific sensor. # noqa: E501

    :param sensor: The ID of the sensor
    :type sensor: str

    :rtype: Measure
    """
    return 'do some magic!'
