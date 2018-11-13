from flask_restful import Resource
from flask import request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.game import GameModel
from model.booth import BoothModel
from docs.booth import BOOTH_POST, BOOTH_GET, BOOTH_PUT


class Booth(Resource):

    # 수정 요함
    @jwt_required
    @swag_from(BOOTH_POST)
    def post(self):
        payload = request.json
        game_ = payload['game']
        name_ = payload['boothName']
        next_time_ = payload['nextCaptureTime']

        BoothModel(game=game_, boothName=name_, nextCaptureTime=next_time_).save()
        return {"status": "Successfully inserted problem information."}

    @jwt_required
    @swag_from(BOOTH_GET)
    def get(self):
        return [{
            "game": booth.game,
            "booth_name": booth.Name,
            "own_team": booth.ownTeam,
            "next_time": booth.nextCaptureTime
        } for booth in BoothModel.objects(game=GameModel.objects(owner=get_jwt_identity()))]

    @swag_from(BOOTH_PUT)
    def put(self):
        payload = request.json
        game_ = payload['game']
        name_ = payload['boothName']
        own_ = payload['ownTeam']
        next_time_ = payload['nextCaptureTime']

        if name_ and (game_ or own_ or next_time_):
            if game_:
                BoothModel.objects(boothName=name_).update_one(set__game=game_)
            if own_:
                BoothModel.objects(boothName=name_).update_one(set__ownTeam=own_)
            if next_time_:
                BoothModel.objects(boothName=name_).update_one(set__nextCaptureTime=next_time_)

            return {"status": "Successfully changed booth information."}, 201
        else:
            return {"status": "No booths to modify"}, 204
