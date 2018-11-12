from flask import request, abort, Response
from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token

from docs.authorization import LOGIN_POST, SIGN_UP_POST
from model.user import UserModel


class Login(Resource):

    @swag_from(LOGIN_POST)
    def post(self):
        payload = request.json
        userID_ = payload['userId']
        PW_ = payload['password']

        for user in UserModel.objects:
            print(user)

        if UserModel.objects(userId=userID_, password=PW_):
            return {
                'access_token': create_access_token(userID_),
                'refresh_token': create_refresh_token(userID_)
            }, 201
        else:
            return abort(401)


class SignUp(Resource):

    @swag_from(SIGN_UP_POST)
    def post(self):
        payload = request.json
        userID_ = payload['userId']
        PW_ = payload['password']
        email_ = payload['email']

        if UserModel.objects(userId=userID_):
            return Response('중복된 ID', 204)

        UserModel(userId=userID_, password=PW_, email=email_, userType=2).save()

        return Response('회원가입 성공', 201)

