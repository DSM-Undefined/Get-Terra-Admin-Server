from datetime import datetime
from flask import request, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.adminUser import AdminUserModel
from model.game import GameModel
from docs.setUp import TIME_SET_PUT


class TimeSet(Resource):

    @jwt_required
    @swag_from(TIME_SET_PUT)
    def put(self):
        payload = request.json
        start_ = datetime.strptime(payload['start'], '%Y-%m-%d %H:%M:%S')
        end_ = datetime.strptime(payload['end'], '%Y-%m-%d %H:%M:%S')

        if start_ < datetime.now() or end_ < datetime.now():
            return Response('현재보다 오래된 시간을 감지했습니다. 다시 요청하세요.', 406)

        user = AdminUserModel.objects(userId=get_jwt_identity()).first()

        GameModel(
            gameKey=user['game'].id,
            start_time=start_,
            end_time=end_,
            teamCount=4
                  ).save()

        return {"status": "success"}, 201
