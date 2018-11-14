import sys

from flask_restful import Resource
from flask import request, Response, jsonify, abort
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import uni_json
from model.game import GameModel
from model.booth import BoothModel
from model.adminUser import AdminUserModel
from docs.booth import BOOTH_POST, BOOTH_GET, BOOTH_PUT


class Booth(Resource):

    # 수정 요함
    @jwt_required
    @swag_from(BOOTH_POST)
    def post(self):
        edits_ = request.json['edits']  # boothName
        print('====================[REQUESTS]====================', file=sys.stderr)
        print(edits_, file=sys.stderrls)
        game_ = AdminUserModel.objects(userId=get_jwt_identity()).first()['game']

        for array in edits_:
            BoothModel(
                game=game_,
                boothName=array['boothName']
            ).save()

        return {"status": "Successfully inserted problem information."}, 201

    @jwt_required
    @swag_from(BOOTH_GET)
    def get(self):
        admin_ = AdminUserModel.objects(userId=get_jwt_identity()).first()['game']
        return uni_json([{
            "bootName": booth.boothName,
            "ownTeam": booth.ownTeam
        } for booth in BoothModel.objects(game=admin_)])
