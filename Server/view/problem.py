from flask_restful import Resource
from flasgger import swag_from

from docs.problem import PROBLEM_GET, PROBLEM_POST, PROBLEM_PUT


class Problem(Resource):

    @swag_from(PROBLEM_POST)
    def post(self):
        pass

    @swag_from(PROBLEM_GET)
    def get(self):
        pass

    @swag_from(PROBLEM_PUT)
    def put(self):
        pass
