from flasgger import swag_from
from flask_restful import Resource

from docs.user import TEAM_POST, TIME_SET_POST


class TeamSet(Resource):

    @swag_from(TEAM_POST)
    def post(self):
        pass


class TimeSet(Resource):
    @swag_from(TIME_SET_POST)
    def post(self):
        pass
