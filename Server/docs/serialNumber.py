SERIAL_NUMBER_GET = {
    "tags": ['SerialNumber'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'description': "게임 진행에 필요한 인증 코드 발급",
    'responses': {
        '201': {
            'description': '인증 코드 발급 성공',
            'example': {
                "serial_number": "029183"
            }
        },
        '403': {
            'description': '인가 실패'
        },
        '401': {
            'description': "인증 코드 발급 도중 문제 발생"
        }
    }
}

SERIAL_CHECK_POST = {
    "tags": ['SerialNumber'],
    'parameters': [
        {
            'name': 'serial_code',
            'description': "인증 코드",
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'description': "[ ONLY_APP | 인증 코드 확인(게임 정보 얻기) ]",
    'responses': {
        '201': {
            'description': '인증 코드 확인 성공',
            'example': {
                "": {
                    "game_number": "109284",
                    "game_owner": "최이삭",
                    "start_time": "2018-11-07 09:46:06.675760",
                    "end_time": "2018-11-23 09:46:06.675760"}
            }
        },
        '403': {
            'description': '확인되지 않은 인증코드'
        },
        '401': {
            'description': "인증 코드 확인 도중 문제 발생"
        }
    }
}
