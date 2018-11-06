from flasgger import swag_from
from flask_restful import Resource

from docs.current import CURRENT_BOOTH_GET, CURRENT_RANKING_GET


class CurrentBooth(Resource):

    @swag_from(CURRENT_BOOTH_GET)
    def get(self):
        pass


class CurrentRanking(Resource):

    @swag_from(CURRENT_RANKING_GET)
    def get(self):
        pass
