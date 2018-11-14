from . import param, n_param

BOOTH_POST = {
    'tags': ['Booth'],
    'description': '부스 정보 입력',
    'parameters': [
        param('game', '게임 정보'),
        param('boothName', '부스 이름'),
        n_param('nextCaptureTime', 'NEXT_CAPTURE_TIME')
    ],
    'responses': {
        '201': {
            'description': '부스 관련 정보 입력 성공',
            'example': {
                "status": "Successfully inserted problem information."
            }
        },
        '401': {
            'description': '업로드 도중 문제 발생'
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
                "game": "게임 정보 반환",
                "boothName": "부스 이름",
                "ownTeam": "부스를 점령한 팀",
                "nextCaptureTime": "NEXT_CAPTURE_TIME"
            }
        },
        '401': {
            'description': '반환 도중 문제 발생'
        }
    }
}

BOOTH_PUT = {
    'tags': ['Booth'],
    'description': '부스 정보 수정(edit)',
    'parameters': [
        param('boothName', '수정할 부스의 이름(이름은 변경 불가)'),
        n_param('game', "게임 정보 변경"),
        n_param('ownTeam', '부스를 점령한 팀 변경'),
        n_param('nextCaptureTime', 'NEXT_CAPTURE_TIME 변경')
    ],
    'responses': {
        '201': {
            'description': '부스 정보 수정 완료',
            'example': {
                "status": "Successfully changed booth information."
            }
        },
        '204': {
            'description': '수정 중 문제 발생',
            'example': {
                "status": "No booths to modify"
            }
        },
        '405': {
            'description': '잘못된 입력 정보'
        }
    }
}
