from flask_restful import Resource


class Problem(Resource):

    def post(self):
        """
        API for managing problems
        """