from . import param, n_param

BOOTH_POST = {
    'tags': ['Booth'],
    'description': '부스 정보 입력',
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        },
        param('edits', '수정할 내용, 필시 아래 항목들을 리스트에 넣어서 보낼 것'),
        n_param('boothName', '부스 이름')
    ],
    'responses': {
        '201': {
            'description': '부스 관련 정보 입력 성공',
            'example': {
                "status": "Successfully inserted problem information."
            }
        },
        '401': {
            'description': '자격 증명 실패'
        }
    }
}

BOOTH_GET = {
    'tags': ['Booth'],
    'description': '부스 목록 반환(return) | request 없음',
    'responses': {
        '201': {
            'description': '부스 목록 반환 성공',
            'examples': {
                "": [{
                    "game": "게임 정보 반환",
                     "boothName": "부스 이름",
                     "ownTeam": "부스를 점령한 팀",
                     "nextCaptureTime": "NEXT_CAPTURE_TIME"
                     }]
            }
        },
        '401': {
            'description': '반환 도중 문제 발생'
        }
    }
}
