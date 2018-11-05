from flask_restful import Resource
from flasgger import swag_from

from docs.icon import ICON_GET


class Icon(Resource):

    @swag_from(ICON_GET)
    def get(self):
        pass
