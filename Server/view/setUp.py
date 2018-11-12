from datetime import datetime
from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import create_game_key, create_team_key
from model.team import TeamModel
from model.game import GameModel
from docs.setUp import TEAM_POST, TIME_SET_POST


class GameSet(Resource):

    @jwt_required
    def post(self):
        payload = request.json
        name_ = payload['name']

        if GameModel.objects(gameName=name_).first():
            return {"status": "The game name has already exists."}

        GameModel(
            gameKey=create_game_key(),
            gameName=name_,
            teamCount=12,
            owner=get_jwt_identity()
        ).save()

        return {"status": "success"}, 201


class TeamSet(Resource):

    @jwt_required
    @swag_from(TEAM_POST)
    def post(self):
        payload = request.json
        game_ = payload['game']
        color_ = payload['color']

        TeamModel(
            game=game_,
            teamId=create_team_key(),
            teamColor=color_
        )


class TimeSet(Resource):

    @jwt_required
    @swag_from(TIME_SET_POST)
    def put(self):
        payload = request.json
        key_ = payload['gameKey']
        start_ = payload['start']
        end_ = payload['end']

        if not GameModel.objects(gameKey=key_).first():
            return {"status": "Key does not exist."}

        GameModel.objects(gameKey=key_).update_one(
            set__start_time=datetime.strptime(start_, '%Y-%m-%d %H:%M:%S'),
            set__end_time=datetime.strptime(end_, '%Y-%m-%d %H:%M:%S')
        )

        return {"status": "success"}, 201
