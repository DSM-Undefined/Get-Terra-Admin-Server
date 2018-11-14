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
        payload = request.json
        game_ = payload['game']
        type_ = payload['type']
        content_ = payload['content']
        answer_ = payload['answer']
        choices_ = payload['choices']

        if ProblemModel.objects(content=content_).first():
            return {'status': 'This Question does already exist.'}, 409

        ProblemModel(
            game=game_,
            problemId=create_problem_key(),
            problemType=type_,
            content=content_,
            answer=answer_,
            choices=choices_
        ).save()
        return {"status": "Successfully inserted booth information."}, 201

    @jwt_required
    @swag_from(PROBLEM_GET)
    def get(self):
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()
        return [{
            "game": problem.game,
            "problemId": problem.Name,
            "problemType": problem.ownTeam,
            "content": problem.nextCaptureTime,
            "answer": problem.answer,
            "choices": problem.choices
        } for problem in ProblemModel.objects(game=GameModel.objects(owner=user))], 201

    @jwt_required
    @swag_from(PROBLEM_PUT)
    def put(self):
        payload = request.json
        game_ = payload['game']
        problem_id_ = payload['problemId']
        type_ = payload['type']
        content_ = payload['content']
        answer_ = payload['answer']
        choices_ = payload['choices']

        if ProblemModel.objects(content=content_).first():
            return {'status': 'This Question does already exist.'}, 409

        elif problem_id_ and (game_ or type_ or content_ or answer_ or choices_):
            if game_:
                ProblemModel.objects(problemId=problem_id_).update_one(set__game=game_)
            if type_:
                ProblemModel.objects(problemId=problem_id_).update_one(set__type=type_)
            if content_:
                ProblemModel.objects(problemId=problem_id_).update_one(set__content=content_)
            if answer_:
                ProblemModel.objects(problemId=problem_id_).update_one(set__answer=answer_)
            if choices_:
                ProblemModel.objects(problemId=problem_id_).update_one(set__choices=choices_)
            return {"status": "Successfully changed information the problems."}, 201

        else:
            return {"status": "No problems to modify"}, 204
