from flask import request, abort, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from docs.authorization import LOGIN_POST, SIGN_UP_POST
from model.adminUser import AdminUserModel


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

        if AdminUserModel.objects(userId=ID_).first():
            return {"status": "The ID already exists."}, 409

        AdminUserModel(userId=ID_, password=PW_).save()

        return Response('회원가입 성공', 201)

