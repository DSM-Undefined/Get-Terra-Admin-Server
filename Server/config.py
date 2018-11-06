from datetime import datetime


class Config:

    SWAGGER = {
        'title': 'Get Terra Admin',
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': 'Get Terra Admin Only API',
            'version': '0.10.0',
            'description': 'Get Terra 서비스의 어드민 전용 API입니다. 현재 개발 및 테스트 중입니다.'
        },
        'host': 'localhost:5000',
        'basePath': '/',
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': 'Booth',
                'description': '부스 운영에 관한 API'
            },
            {
                'name': 'Problem',
                'description': '문제에 관한 API'
            },
            {
                'name': 'Icon',
                'description': '각 부스별 고유 QR코드 부여에 관한 API'
            },
            {
                'name': 'Authorization',
                'description': '로그인 및 회원가입에 관한 API'
            },
            {
                'name': 'SerialNumber',
                'description': '플레이어가 게임에 참여할 때 사용되는 인증 코드를 발급하는 API'
            },
            {
                'name': 'Status',
                'description': '부스에 대한 정보를 실시간으로 전달하는 API'
            },
            {
                'name': 'SetUp',
                'description': '팀 설정, 게임 시작/종료 시간을 설정하는 API'
            }
        ]
    }

    JSON_AS_ASCII = False

    started_point = datetime.now()
