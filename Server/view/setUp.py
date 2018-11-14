from datetime import datetime
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import create_game_key, create_team_key
from model.team import TeamModel
from model.adminUser import AdminUserModel
from model.game import GameModel
from docs.setUp import TEAM_POST, TIME_SET_PUT


class TimeSet(Resource):

    @jwt_required
    @swag_from(TIME_SET_PUT)
    def put(self):
        payload = request.json
        start_ = payload['start']
        end_ = payload['end']
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()

        GameModel(
            gameKey=int(user['game']),
            start_time=datetime.strptime(start_, '%Y-%m-%d %H:%M:%S'),
            end_time=datetime.strptime(end_, '%Y-%m-%d %H:%M:%S'),
            teamCount=4
                  ).save()

        return {"status": "success"}, 201
