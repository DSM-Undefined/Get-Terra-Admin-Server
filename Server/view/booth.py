from pymongo import MongoClient
from flask_restful import Resource
from flask import jsonify
from flasgger import swag_from

from docs.booth import BOOTH_POST, BOOTH_GET, BOOTH_PUT


class Booth(Resource):

    @swag_from(BOOTH_POST)
    def post(self):
        pass

    @swag_from(BOOTH_GET)
    def get(self):
        dummy_output = [
            {
                "booth_num": "1",
                "booth_name": "UNDEFINED",
                "booth_owner": "소준호(선배님)"
            },
            {
                "booth_num": "2",
                "booth_name": "동근이네 방",
                "booth_owner": "최이삭"
            },
            {
                "booth_num": "3",
                "booth_name": "1학년1반",
                "booth_owner": "비선실세 유동근"
            }
        ]

        return jsonify(dummy_output)

    @swag_from(BOOTH_PUT)
    def put(self):
        pass
