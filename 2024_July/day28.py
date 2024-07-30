# 14-1.Data Pretty Printer_Q
# # pprint : Python 데이터 구조를 예쁘게 인쇄할 때 사용하는 기능 제공
# depth(중첩 데이터), indent(들여쓰기), width(줄 길이 조정), sort_dicts(키 정렬), stream(파일에 출력) 옵션 제공

# from urllib import request
# import json

# response = request.urlopen("https://jsonplaceholder.typicode.com/users")

# response_json = response.read()

# d = json.loads(response_json)

# from pprint import pprint
# pprint(d)

# 15-1.Iterate Dictionary_Q
# 아래와 같은  딕셔너리(Dict) 를 출력 결과 와 같이 완성 하세요. (반복문 사용)
# Dict 선언
d = dict(one = list(range(1, 11)), two = list(range(11, 23)), three = list(range(23, 37)))

# 출력 결과 
# key 'one' has values [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> total : 10
# key 'two' has values [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] -> total : 12
# key 'three' has values [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36] -> total : 14

# 방법1 
for k, v in d.items():
    print(f'key "{k}" has values {v} -> total : {len(v)}')

# 방법2 Iterator 활용 하기. 


# Iterator : 순서대로 다음에 값을 반환(리턴)할 수 있는 객체 또는 상태(자체적으로 next 메소드 내장)
#            반복가능한 객체, 순회하면서 처리
# dict 구조의 items(), keys(), get() 함수를 기억해야 되요.
# https://www.w3schools.com/python/python_ref_dictionary.asp