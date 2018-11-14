from docs import param
TEAM_POST = {
    'tags': ['SetUp'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('teamId', '팀 ID'),
        param('teamColor', '팀 색상 | 색상 예시: #')
    ],
    'description': '팀 설정',
    'responses': {
        '201': {
            'description': '팀 설정 완료'
        },
        '401': {
            'description': '정보 전달 실패'
        }
    }
}

TIME_SET_PUT = {
    'tags': ['SetUp'],
    'description': '게임 시작, 종료 시간 설정',
    'parameters': [
        param('start', '시작 시간'),
        param('end', '종료 시간')
    ],
    'responses': {
        '201': {
            'description': '정보 전달 성공'
        },
        '401': {
            'description': '정보 전달 실패'
        }
    }
}
