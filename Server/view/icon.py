import shutil
import os
import zipfile
import qrcode
import qrcode.image.svg
# pillow 설치 필요

from flasgger import swag_from
from flask import send_file
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from docs.icon import ICON_GET
from model.adminUser import AdminUserModel
from model.booth import BoothModel


class Icon(Resource):

    @jwt_required
    @swag_from(ICON_GET)
    def get(self):
        factory = qrcode.image.svg.SvgImage
        game_ = AdminUserModel.objects(userId=get_jwt_identity()).first().game

        directory = 'static/qr/' + str(game_.gameKey)
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.makedirs(directory)
        directory += '\\'

        zip = zipfile.ZipFile(directory + 'qr.zip', 'w')
        for booth in BoothModel.objects(game=game_):
            file_name = directory+booth.boothName+'.svg'
            qrcode.make(booth.boothName, image_factory=factory).save(file_name)

            zip.write(file_name, booth.boothName+'.svg', compress_type=zipfile.ZIP_DEFLATED)
        zip.close()

        return send_file(directory + 'qr.zip', mimetype='application/zip')
