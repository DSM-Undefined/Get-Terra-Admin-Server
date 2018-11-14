import json
from random import randint
from flask import Response

from model.problem import ProblemModel
from model.game import GameModel
from model.team import TeamModel


def create_game_key():
    key = randint(100000, 1000000)
    while GameModel.objects(gameKey=key).first():
        key = randint(100000, 1000000)

    return key


def create_team_key():
    key = randint(100000, 1000000)
    while TeamModel.objects(teamId=key).first():
        key = randint(100000, 1000000)

    return key


def create_problem_key():
    key = randint(100000, 1000000)
    while ProblemModel.objects(problemId=key).first():
        key = randint(100000, 1000000)

    return key


def uni_json(data, status_code=201):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status_code,
        content_type='application/json; charset=utf8'
    )
