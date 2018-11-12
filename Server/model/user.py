from mongoengine import *

from model.game import GameModel


class UserModel(Document):
    """
    사용자 정보 관련 Collection
    """

    meta = {
        'collection': 'user'
    }

    game = ReferenceField(
        document_type=GameModel,
        reverse_delete_rule=CASCADE
    )

    userId = StringField(
        primary_key=True
    )

    email = StringField(
        required=True
    )

    password = StringField(
        required=True
    )

    team = ReferenceField(
        document_type='TeamModel'
    )

    # 유저타입 관련( 1: 플레이어 | 2: 어드민 )
    userType = IntField(
        required=True
    )
