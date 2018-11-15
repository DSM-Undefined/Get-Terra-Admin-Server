from docs import param

TIME_SET_PUT = {
    'tags': ['SetUp'],
    'description': '게임 시작, 종료 시간 설정',
    'parameters': [
        param('start', '시작 시간'),
        param('end', '종료 시간')
    ],
    'responses': {
        '201': {
            'description': '정보 전달 성공'
        },
        '406': {
            'description': '현재보다 오래된 시간 감지'
        }
    }
}
