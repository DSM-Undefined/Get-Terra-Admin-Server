from . import param

AUTHORIZATION_POST = {
    'tags': ['Authorization'],
    'parameters': [
        param('usedId', "user's ID"),
        param('password', "비밀번호")
    ],
    'responses': {
        '201': {
            'description': "JWT 반환 성공",
            "example": {
                "": {
                    "access_token": "dkAhffkDkanxmsJWTzhemdla",
                    "refresh_token": "flvmfptlxhzms"
                }
            }
        },
        '401': {
            'description': "자격 증명 과정 중 문제 발생"
        },
        '403': {
            'description': "자격 증명 실패"
        }
    }
}

SIGN_UP_POST = {
    'tags': ['Authorization'],
    'description': '회원가입',
    'parameters': [
        param('userId', "user's ID"),
        param('password', "비밀번호"),
        param('email', "이메일")
    ],
    'responses': {
        '201': {
            'description': "회원가입 성공"
        },
        '401': {
            'description': "회원가입 도중 문제 발생"
        },
        '409': {
            'description': "중복된 계정 감지"
        }
    }

}