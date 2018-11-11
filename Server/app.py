from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from mongoengine import connect

from config import Config


def make_app() -> Flask:
    app: Flask = Flask(__name__)
    api: Api = Api(app)
    app.config.from_object(Config)
    connect('localhost')    # 테스트시에는 Atlas 사용
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    from view.booth import Booth
    api.add_resource(Booth, '/booth')

    from view.authorization import Authorization, SignUp
    api.add_resource(Authorization, '/login')
    api.add_resource(SignUp, '/signup')

    from view.problem import Problem
    api.add_resource(Problem, '/problem')

    from view.icon import Icon
    api.add_resource(Icon, '/icon')

    from view.serialNumber import SerialCheck, SerialNumber
    api.add_resource(SerialNumber, '/session/new')  # 인증코드 발급 uri
    api.add_resource(SerialCheck, '/session/check')  # 인증코드 확인 uri(ONLY_USER_APP)

    from view.user import TeamSet, TimeSet
    api.add_resource(TeamSet, '/set-team')
    api.add_resource(TimeSet, '/set-time')

    from view.status import CurrentBooth, CurrentRanking
    api.add_resource(CurrentBooth, '/status/booth')
    api.add_resource(CurrentRanking, '/status/ranking')

    return app
