from docs import param, n_param

PROBLEM_GET = {
    'tags': ['Problem'],
    'description': '전체 문항 반환',
    'parameters': [{
        'name': 'jwt_header',
        'description': 'JWT',
        'in': 'header',
        'type': 'str',
        'required': True
    }],
    'responses': {
        '201': {
            'description': '문항 반환 성공',
            'example': [
                {
                    'game': "최이삭의 게임",
                    'problemId': "문항번호",
                    'problemType': "문항 종류",
                    'content': "문제",
                    'answer': '정답',
                    'choices': '선택지'
                }
            ]
        },
        '401': {
            'description': '문항 반환 실패'
        }
    }
}

PROBLEM_POST = {
    'tags': ['Problem'],
    'description': '문항 정보 입력',
    'parameters': [
        param('game', '게임'),
        param('type', '문항 종류'),
        param('content', '문제'),
        param('answer', '정답'),
        n_param('choices', '선택지')
    ],
    'responses': {
        '201': {
            'description': '문제 입력 성공',
            'example': {
                "status": "Successfully inserted booth information."
            }
        },
        '401': {
            'description': '문제 입력 실패'
        },
        '409': {
            'description': '중복된 문항 감지',
            'example': {
                'status': 'This Question does already exist.'
            }
        }
    }
}

PROBLEM_PUT = {
    'tags': ['Problem'],
    'description': '문항 정보 수정\n'
                   """{
                        "problemId": "수정할 문항의 번호",
                        "content": "수정할 문제",
                        "answer": "수정할 정답",
                        "type": "(1: 객관식, 2: OX문제)",
                        "choices": {
                            "first": "수정할 1번 선택문",
                            "second": "수정할 2번 선택문",
                            "third": "수정할 3번 선택문",
                            "fourth": "수정할 4번 선택문"
                            } 
                        }""",
    'parameters': [
        param('problemId', '수정할 문항 번호'),
        n_param('game', '수정할 게임의 내용'),
        n_param('type', '문항 종류'),
        n_param('content', '문제'),
        n_param('answer', '정답'),
        n_param('choices', '선택지')
    ],
    'responses': {
        '201': {
            'description': '문제 수정 성공',
            'example': {"status": "Successfully changed information the problems."}
        },
        '204': {
            'description': '수정할 문항의 번호 없음',
            'example': {"status": "No problems to modify"}
        },
        '409': {
            'description': '중복된 문항 감지',
            'example': {'status': 'This Question does already exist.'}
        }
    }
}
