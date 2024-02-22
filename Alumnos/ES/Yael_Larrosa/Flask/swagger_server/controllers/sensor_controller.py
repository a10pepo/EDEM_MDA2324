import connexion
import six

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server.models.nuevamedicion import Nuevamedicion  # noqa: E501
from swagger_server import util


def add_new_measure(body):  # noqa: E501
    """Añadir una nueva medición de temperatura

     # noqa: E501

    :param body: Datos de la nueva medición
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Nuevamedicion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def ultimamedidasensor(sensor):  # noqa: E501
    """Obtener la última medición de temperatura por sensor

     # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Medicion
    """
    return 'do some magic!'
