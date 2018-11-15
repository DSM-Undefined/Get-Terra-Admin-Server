import os
import zipfile
import qrcode
# pillow 설치 필요

from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from docs.icon import ICON_GET
from model.adminUser import AdminUserModel
from model.booth import BoothModel


class Icon(Resource):

    @jwt_required
    @swag_from(ICON_GET)
    def get(self):
        game_ = AdminUserModel.objects(userId=get_jwt_identity()).first()['game']
        var = [qrcode.make(booth.boothName) for booth in BoothModel.objects(game=game_)]
        return var
