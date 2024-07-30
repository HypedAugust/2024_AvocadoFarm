# 많이 쓰이는 매소드

# replace 
# print("hello".replace("l", 'w'))

# strip()
# print(" hello ".strip())

# split()
# print("hello world".split("hello", "world"))

# upper, lower

# text = "hello, world!"
# new_text = text.strip().lower().replace(',','').split
# print(new_text)

# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 
# 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 
# return하도록 solution 함수를 완성해주세요.

def solution(s1, s2):
    answer = 0 
    for word in s1:
        if word in s2:
            answer += 1
    return answer

def solution(s1, s2):
    return len(set(s1)&set(s2))

s1 = ["apple", "banana", "cherry"]
s2 = ["banana", "cherry", "date"]
result = solution(s1, s2)
print(result)

# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
# num_list의 원소의 순서를 거꾸로 
# 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.

# [::-1]
def solution(num_list):
    return num_list[::-1]

# 문자열 뒤집기도 마찬가지 
def solution(num_list):
    return num_list[::-1]