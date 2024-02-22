import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response400 import InlineResponse400  # noqa: E501
from swagger_server.models.inline_response404 import InlineResponse404  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor_sensor_get(sensor):  # noqa: E501
    """Obtener la última medición por sensor

    A través de este método, se obtendrán las observaciones más recientes de los sensores, incluyendo cómo deben proporcionarse los parámetros y qué respuestas cabe esperar en diferentes situaciones.  # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
