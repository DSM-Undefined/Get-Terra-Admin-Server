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
        if AdminUserModel.objects(userId=get_jwt_identity()):    # 유저가 회원가입되어 있으면
            return [{
                'boothName': booth.boothName,
                'ownTeam': booth.ownTeam
            } for booth in BoothModel.objects(
                game=GameModel.objects(
                    owner=get_jwt_identity()
                ).first()
            )], 201                                         # 부스 점령 현황 반환(201)


class CurrentRanking(Resource):

    @jwt_required
    @swag_from(CURRENT_RANKING_GET)
    def get(self):
        ret = []
        game_ = GameModel.objects(owner=get_jwt_identity()).first()     # 게임 콜렉션 중에서 owner 가 userId 인 게임 찾기
        total_ = len(BoothModel.objects(game=game_))    # user의 현재 게임 내에 있는 총 부스의 개수
        for team in TeamModel.objects(game=game_):
            # temp 는 team 이 점령한 부스의 개수를 지칭
            temp = len(BoothModel.objects(ownTeam=TeamModel.objects(teamId=team.teamId).first()))
            ret.append({
                "teamId": team.teamId,
                "ownCount": temp,
                "percent": temp / total_ * 100
            })

        return ret, 201     # for 문이 끝나고 ret 반환
