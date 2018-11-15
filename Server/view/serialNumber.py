from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from model.adminUser import AdminUserModel
from docs.serialNumber import SERIAL_NUMBER_GET


class SerialNumber(Resource):

    @jwt_required
    @swag_from(SERIAL_NUMBER_GET)
    def get(self):
        user_self = AdminUserModel.objects(userId=get_jwt_identity()).first()
        if user_self:
            return {"serial_number": user_self['game'].id}
