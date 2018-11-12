from flask import request
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.game import GameModel
from model.user import UserModel
from docs.serialNumber import SERIAL_NUMBER_GET, SERIAL_CHECK_POST


class SerialNumber(Resource):

    @jwt_required
    @swag_from(SERIAL_NUMBER_GET)
    def get(self):
        if UserModel.objects(userId=get_jwt_identity()).first():
            key = GameModel.objects(owner=get_jwt_identity()).first()
            return {"serial_number": key.gameKey}


class SerialCheck(Resource):

    @swag_from(SERIAL_CHECK_POST)
    def post(self):
        payload = request.json
        num_ = payload['serialCode']

        temp = GameModel.objects(gameKey=num_).first()
        if not temp:
            return {"status": "serial code does not exist."}
        else:
            return {
                "startTime": str(temp.start_time),
                "endTime": str(temp.end_time),
                "owner": temp.owner,
                "gameName": temp.gameName,
                "teamCount": temp.teamCount
            }, 201
