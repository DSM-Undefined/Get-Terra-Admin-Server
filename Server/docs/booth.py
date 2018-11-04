from . import param, n_param

BOOTH_POST = {
    'tags': ['Booth'],
    'description': '부스 정보 입력',
    'parameters': [
        param('number', '부스 번호(추후 변경될 수 있음 | 고유 QR코드 이미지 조회시 사용됨)'),
        param('name', '부스 이름'),
        param('owner', '부스 운영진 혹은 주최')
    ],
    'responses': {
        '201': {
            'description': '부스 관련 정보 입력 성공'
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
                '': {
                    'booth_num': "1",
                    "booth_name": "UNDEFINED",
                    "booth_owner": "김철수"
                }
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
        param('num', '수정할 부스의 번호'),
        n_param('name', '바꿀 부스의 새 이름'),
        n_param('owner', '바꿀 부스의 운영진')
    ],
    'responses': {
        '201': {
            'description': '부스 정보 수정 완료'
        },
        '401': {
            'description': '수정 중 문제 발생'
        },
        '405': {
            'description': '잘못된 입력 정보'
        }
    }
}
