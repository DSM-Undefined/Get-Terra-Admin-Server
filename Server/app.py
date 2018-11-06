from flask import Flask, current_app
from flask_restful import Api
from flasgger import Swagger

from config import Config
from view.booth import Booth
from view.problem import Problem
from view.icon import Icon
from view.authorization import Authorization, SignUp
from view.serialNumber import SerialNumber
from view.user import TeamSet, TimeSet


def make_app() -> Flask:
    app: Flask = Flask(__name__)
    api: Api = Api(app)
    app.config.from_object(Config)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    api.add_resource(Booth, '/booth')
    api.add_resource(Problem, '/problem')
    api.add_resource(Icon, '/icon')
    api.add_resource(Authorization, '/login')
    api.add_resource(SignUp, '/signup')
    api.add_resource(SerialNumber, '/session/new')  # 인증코드 발급 uri
    api.add_resource(TeamSet, '/set-team')
    api.add_resource(TimeSet, '/set-time')

    return app
