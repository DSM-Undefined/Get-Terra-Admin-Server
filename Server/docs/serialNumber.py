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
