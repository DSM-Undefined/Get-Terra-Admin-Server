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
            }
        ]
    }

    JSON_AS_ASCII = False

    started_point = datetime.now()