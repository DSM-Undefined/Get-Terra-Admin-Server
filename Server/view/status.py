from flasgger import swag_from
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from docs.status import CURRENT_BOOTH_GET, CURRENT_RANKING_GET

from model.team import TeamModel
from model.adminUser import AdminUserModel
from model.game import GameModel
from model.booth import BoothModel


class CurrentBooth(Resource):

    @jwt_required
    @swag_from(CURRENT_BOOTH_GET)
    def get(self):
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()
        if user:    # 유저가 회원가입되어 있으면
            return [{
                'boothName': booth.boothName,
                'ownTeam': booth.ownTeam
            } for booth in BoothModel.objects(game=user['game'].id)], 201
            # 부스 점령 현황 반환(201)


class CurrentRanking(Resource):

    @jwt_required
    @swag_from(CURRENT_RANKING_GET)
    def get(self):
        ret = []
        user = AdminUserModel.objects(userId=get_jwt_identity()).first()

        total_ = len(BoothModel.objects(game=user['game'].id))    # user의 현재 게임 내에 있는 총 부스의 개수
        for team in TeamModel.objects(game=user['game'].id):
            # temp 는 해당 team 이 점령한 부스의 개수를 지칭
            temp = len(BoothModel.objects(ownTeam=TeamModel.objects(teamId=team.teamId).first()))
            ret.append({
                "teamId": team.teamId,
                "ownCount": temp,
                "percent": temp / total_ * 100
            })

        return ret, 201     # for 문이 끝나고 ret 반환
