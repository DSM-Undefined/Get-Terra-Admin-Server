
PROBLEM_GET = {
    'tags': ['Problem'],
    'description': '전체 문항 반환',
    'responses': {
        '201': {
            'description': '문항 반환 성공'
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
        {
            'name': 'questions',
            'description': """문항 정보(예시는 다음과 같음)\n{
                        "question": "대한민국에 최초로 세워진 소프트웨어 마이스터 고등학교는?",
                        "answer": 1,
                        "type": "1(1: 객관식, 2: OX문제)",
                        "choices": {
                            "first": "대덕소프트웨어마이스터고등학교",
                            "second": "대구소프트웨어마이스터고등학교",
                            "third": "광주소프트웨어마이스터고등학교",
                            "fourth": "선린인터넷고등학교"
                        }
                    }""",
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '문제 입력 성공'
        },
        '401': {
            'description': '문제 입력 실패'
        },
        '409': {
            'description': '중복된 문항 감지'
        }
    }
}

PROBLEM_PUT = {
    'tags': ['Problem'],
    'description': '문항 정보 수정',
    'parameters': [
        {
            'name': 'alter',
            'description': """수정할 내용(객관식인 경우에만 choices 사용)\n{
                        "number": "수정할 문항의 번호",
                        "question": "수정할 문제",
                        "answer": "수정할 정답",
                        "type": "(1: 객관식, 2: OX문제)",
                        "choices": {
                            "first": "수정할 1번 선택문",
                            "second": "수정할 2번 선택문",
                            "third": "수정할 3번 선택문",
                            "fourth": "수정할 4번 선택문"
                        }
                    }""",
            'in': 'json',
            'type': 'str',
            'required': True
        }
    ],
    'responses': {
        '201': {
            'description': '문제 수정 성공'
        },
        '401': {
            'description': '문제 수정 실패'
        },
        '409': {
            'description': '중복된 문항 감지'
        }
    }
}
