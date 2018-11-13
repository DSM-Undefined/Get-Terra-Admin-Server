CURRENT_BOOTH_GET = {
    'tags': ['Status'],
    'parameters': [
        {
            'name': 'jwt_header',
            'description': 'JWT',
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'description': '현재 부스를 어떤 팀이 점령하고 있는지 표시',
    'responses': {
        '201': {
            'description': '정보 전달 성공'
        },
        '401': {
            'description': '정보 전달 실패'
        }
    }
}

CURRENT_RANKING_GET = {
    'tags': ['Status'],
    'description': '등수 표시(점령한 부스의 개수, 퍼센트)',
    'responses': {
        '201': {
            'description': '정보 전달 성공'
        },
        '401': {
            'description': '정보 전달 실패'
        }
    }
}
