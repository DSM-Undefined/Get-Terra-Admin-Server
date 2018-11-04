from flask_restful import Resource
from flasgger import swag_from

from docs.booth import BOOTH_POST, BOOTH_GET, BOOTH_PUT


class Booth(Resource):

    @swag_from(BOOTH_POST)
    def post(self):
        pass

    @swag_from(BOOTH_GET)
    def get(self):
        pass

    @swag_from(BOOTH_PUT)
    def put(self):
        pass
