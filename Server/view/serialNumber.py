from flasgger import swag_from
from flask_restful import Resource


from docs.serialNumber import SERIAL_NUMBER_GET


class SerialNumber(Resource):

    @swag_from(SERIAL_NUMBER_GET)
    def get(self):
        pass
