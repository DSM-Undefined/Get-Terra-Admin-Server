
ICON_GET = {
    'tags': ['Icon'],
    'parameters': [
        {
            'name': 'Authorization',
            'description': "헤더로 jwt 받아오기",
            'in': 'header',
            'type': 'str',
            'required': True
        }
    ],
    'description': 'QR코드 발급',
    'responses': {
        '201': {
            'description': 'QR코드 발급 성공',
            'example': {
                "url": "파일이 있는 url 반환(파일 확장자는 .zip | 추후 변경될 수 있음)"
            }
        },
        '204': {
            'description': "발급할 QR코드가 없거나 혹은 인증 오류 발생"
        },
        '401': {
            'description': "발급 도중 문제 발생"
        }
    }
}
