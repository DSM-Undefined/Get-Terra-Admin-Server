from datetime import datetime
from mongoengine import *


class GameModel(Document):
    meta = {
        'collection': 'game'
    }

    gameKey = IntField(
        primary_key=True
    )

    gameName = StringField(
        required=False
    )

    owner = StringField(
        required=False
    )

    start_time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    end_time = DateTimeField(
        required=True,
        default=datetime.now()
    )

    # 최대 팀 갯수
    teamCount = IntField(
        required=True,
        min_value=0,
        max_value=100
    )
