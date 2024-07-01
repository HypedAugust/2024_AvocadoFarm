## Day 2 
# 두 수의 나눗셈. 다시확인 
def solution(num1, num2):
    return int(num1/num2*1000)

# 숫자 비교하기 
def solution(num1, num2):
    if num1 == num2:
        return 1
    elif num1 != num2:
        return -1

## day3 
# 분수의 덧셈 
import math
def solution(denum1, num1, denum2, num2):
    denum = denum1*num2 + denum2*num1
    num = num1*num2
    gcd = math.gcd(denum,num)
    return[denum//gcd, num//gcd]

# 배열 두배로 만들기
def solution(numbers):
    return[2*i for i in numbers]

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        answer.append(2*numbers[i])
    return answer