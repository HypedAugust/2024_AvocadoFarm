# 구현내용
# 조건1 : 전화번호부 확인
# 조건2 : 전화번호부 멤버 추가
# 조건3 : 전화번호부 멤버 삭제
# 조건4 : 프로그램 종료
# 조건5 : 전화번호 전체 데이터는 아래와 같이 json 형식으로 가정
# 조건6 : (가능한경우) 파일 쓰기, 읽기 기능 추가

import json 
phonebook = {}
phonebook = {
                0: {'Name': 'Kim', 'Phone': '45648733'},
                1: {'Name': 'Lee', 'Phone': '89376333'},
                2: {'Name': 'Park', 'Phone': '36457818'},
                3: {'Name': 'Chung', 'Phone': '76891234'},
                4: {'Name': 'Choi', 'Phone': '67451237'}
            }



def phonebook():
    command = input('명령어 입력: check, d, w, a, end')
    while True:
        if command == 'check':
            if name in phonebook:
                print(f'{name}의 번호는 {phonebook[name]}')
        elif command == 'd':
            name = input('삭제할 이름 작성')
            if name in phonebook:
                del phonebook[name]
                print(f'{name} 삭제완료')
        elif command == 'a':
            name = input('이름 입력')
            phone = input('번호 입력')
            phonebook[name] = phone
            print(f'{name} 추가완료')
        elif command == 'end':
            with open('phonebook.json', 'w') as file:
                json.dump(phonebook, file)
                print('종료완료')
           
        else: 
            print('잘못됨.')
            break
    