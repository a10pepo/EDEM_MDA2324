# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.medicion import Medicion  # noqa: E501
from swagger_server.models.nuevamedicion import Nuevamedicion  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSensorController(BaseTestCase):
    """SensorController integration test stubs"""

    def test_add_new_measure(self):
        """Test case for add_new_measure

        Añadir una nueva medición de temperatura
        """
        body = Nuevamedicion()
        response = self.client.open(
            '/v2/nuevamedicion',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_ultimamedidasensor(self):
        """Test case for ultimamedidasensor

        Obtener la última medición de temperatura por sensor
        """
        response = self.client.open(
            '/v2/obtenerultimamedidasensor/{sensor}'.format(sensor='sensor_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
