from flask import Flask, current_app
from flask_restful import Api
from flasgger import Swagger

from config import Config
from view.booth import Booth


def make_app():
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(Config)
    Swagger(app, template=app.config['SWAGGER_TEMPLATE'])

    api.add_resource(Booth, '/booth')

    return app
