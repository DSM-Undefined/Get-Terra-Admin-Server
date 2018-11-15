from flask_restful import Resource
from flask import request, abort
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import uni_json
from model.booth import BoothModel
from model.team import TeamModel
from model.game import GameModel
from model.adminUser import AdminUserModel
from docs.booth import BOOTH_POST, BOOTH_GET


class Booth(Resource):

    # 수정 요함
    @jwt_required
    @swag_from(BOOTH_POST)
    def post(self):
        edits_ = request.json['edits']  # boothName
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()
        game = user['game'].id

        if not user:
            abort(401)
        else:
            for array in edits_:
                BoothModel(
                    game=game,
                    boothName=array['boothName'],
                    ownTeam=0
                ).save()

            return {"status": "Successfully inserted problem information."}, 201

    @jwt_required
    @swag_from(BOOTH_GET)
    def get(self):
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()
        return uni_json([{
            "bootName": booth.boothName,
            "ownTeam": TeamModel.objects(game=user.game, teamId=booth.ownTeam.teamId).first().teamId
            # "ownTeam": booth.ownTeam.id
        } for booth in BoothModel.objects(game=user['game'])])
