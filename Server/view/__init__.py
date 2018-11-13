from random import randint

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
