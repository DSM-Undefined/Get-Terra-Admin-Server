from flask_restful import Resource
from flask import request
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.game import GameModel
from model.booth import BoothModel
from model.adminUser import AdminUserModel
from docs.booth import BOOTH_POST, BOOTH_GET, BOOTH_PUT


class Booth(Resource):

    # 수정 요함
    @jwt_required
    @swag_from(BOOTH_POST)
    def post(self):
        edits_ = request.json['edits']   # boothName

        for array in edits_:
            BoothModel(
                boothName=array['boothName']
            ).save()

        return {"status": "Successfully inserted problem information."}, 201

    @jwt_required
    @swag_from(BOOTH_GET)
    def get(self):
        admin = AdminUserModel.objects(userId=get_jwt_identity()).first()
        return [{
            "game": booth.game,
            "bootName": booth.boothName,
            "ownTeam": booth.ownTeam
        } for booth in BoothModel.objects(game=admin['game'])], 201

    @swag_from(BOOTH_PUT)
    def put(self):
        edits_ = request.json['edits']

        for r in edits_:
            if r['boothName'] and (r['game'] or r['ownTeam'] or r['nextCaptureTime']):
                if r['game']:
                    BoothModel.objects(boothName=r['boothName']).update_one(set__game=r['game'])
                if r['ownTeam']:
                    BoothModel.objects(boothName=r['boothName']).update_one(set__ownTeam=r['ownTeam'])
                if r['nextCaptureTime']:
                    BoothModel.objects(boothName=r['boothName']).update_one(set__nextCaptureTime=r['nextCaptureTime'])

            return {"status": "Successfully changed booth information."}, 201
        else:
            return {"status": "No booths to modify"}, 204
