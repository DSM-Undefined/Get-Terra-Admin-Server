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
        key_ = payload['gameKey']
        start_ = payload['start']
        end_ = payload['end']

        if not AdminUserModel.objects(userId=get_jwt_identity(), game=key_).first():
            return {"status": "Key does not exist."}

        GameModel.objects(gameKey=key_).update_one(
            set__start_time=datetime.strptime(start_, '%Y-%m-%d %H:%M:%S'),
            set__end_time=datetime.strptime(end_, '%Y-%m-%d %H:%M:%S')
        )

        return {"status": "success"}, 201
