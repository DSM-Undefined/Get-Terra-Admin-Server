from flask import request
from flask_restful import Resource
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity

from view import create_problem_key
from model.problem import ProblemModel
from model.adminUser import AdminUserModel
from model.game import GameModel
from docs.problem import PROBLEM_GET, PROBLEM_POST, PROBLEM_PUT


class Problem(Resource):

    @jwt_required
    @swag_from(PROBLEM_POST)
    def post(self):
        edits_ = request.json['edits']
        user_self = AdminUserModel.objects(userId=get_jwt_identity()).first()['game']

        for r in edits_:
            if ProblemModel.objects(content=r['content']).first():
                return {'exist': r['content']}, 409

            ProblemModel(
                game=user_self,
                problemId=create_problem_key(),
                content=r['content'],
                answer=r['answer'],
                choices=r['choices']
            ).save()

        return {"status": "Successfully inserted quiz information."}, 201

    @jwt_required
    @swag_from(PROBLEM_GET)
    def get(self):
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()
        return [{
            "game": problem.game,
            "problemId": problem.problemId,
            "content": problem.content,
            "answer": problem.answer,
            "choices": problem.choices
        } for problem in ProblemModel.objects(game=user['game'])], 201
