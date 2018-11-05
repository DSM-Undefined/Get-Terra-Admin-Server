from flasgger import swag_from
from flask_restful import Resource

from docs.authorization import AUTHORIZATION_POST, SIGN_UP_POST


class Authorization(Resource):

    @swag_from(AUTHORIZATION_POST)
    def post(self):
        pass


class SignUp(Resource):

    @swag_from(SIGN_UP_POST)
    def post(self):
        pass
