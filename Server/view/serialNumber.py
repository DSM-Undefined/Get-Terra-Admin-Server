from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.game import GameModel
from model.adminUser import AdminUserModel
from docs.serialNumber import SERIAL_NUMBER_GET, SERIAL_CHECK_POST


class SerialNumber(Resource):

    @jwt_required
    @swag_from(SERIAL_NUMBER_GET)
    def get(self):
        user_self = AdminUserModel.objects(userId=get_jwt_identity()).first()
        if user_self:
            return {"serial_number": user_self['game'].id}


class SerialCheck(Resource):

    @swag_from(SERIAL_CHECK_POST)
    def post(self):
        num_ = request.json['serialCode']
        user = AdminUserModel.objects(game=num_).first()
        return user['game']
        game = GameModel.objects(gameKey=user['game'].id)
        if not user:
            return {"status": "serial code does not exist."}
        else:
            return {
                "startTime": GameModel.objects(),
                "endTime": str(GameModel.objects(gameKey=user['game']).first()),
                "teamCount": GameModel.objects(gameKey=user['game']).first()
            }, 201
