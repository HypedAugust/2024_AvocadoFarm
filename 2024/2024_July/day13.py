# 문자열 cipher와 정수 
# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# code가 매개변수로 주어질 때 해독된 암호 문자열을 
# return하도록 solution 함수를 완성해주세요. 


def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer

def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer
                
# 문자열 my_string이 매개변수로 주어질 때, 
# 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 
# return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = ''
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer

def solution(my_string):
    return my_string.swapcase()

# 정수 배열 array가 매개변수로 주어질 때, 
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    answer = []
    biggest = max(array)
    index = array.index(biggest)
    answer = [biggest, index]
    return answer 
