from datetime import datetime
from flask import request, abort, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from . import create_game_key
from docs.authorization import LOGIN_POST, SIGN_UP_POST
from model.adminUser import AdminUserModel
from model.game import GameModel


# 어드민 로그인
class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        userID_ = payload['userId']
        PW_ = payload['password']

        if AdminUserModel.objects(userId=userID_, password=PW_):
            return {
                'access_token': create_access_token(userID_),
                'refresh_token': create_refresh_token(userID_)
            }, 201
        else:
            return abort(401)


# 어드민 회원가입
class SignUp(Resource):

    @swag_from(SIGN_UP_POST)
    def post(self):
        payload = request.json
        ID_ = payload['userId']
        PW_ = payload['password']
        start_ = payload['start']   # '%Y-%m-%d %H:%M:%S' 형식
        end_ = payload['end']       # '%Y-%m-%d %H:%M:%S' 형식

        if AdminUserModel.objects(userId=ID_).first():
            return {"status": "The ID already exists."}, 409

        game = GameModel(
            gameKey=create_game_key(),
            start_time=datetime.strptime(start_, '%Y-%m-%d %H:%M:%S'),
            end_time=datetime.strptime(end_, '%Y-%m-%d %H:%M:%S'),
            teamCount=4
        ).save()
        AdminUserModel(game=game.id, userId=ID_, password=PW_).save()

        return Response('회원가입 성공', 201)

