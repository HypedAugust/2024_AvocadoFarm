# 출생년도 계산 
def solution(age):
    answer = 2022 - int(age) + 1
    return answer 

print(solution(32))

# 배열의 평균값 
def solution(numbers):
    sum = 0 
    for i in numbers: 
        sum += i 
    answer = sum / len(numbers)
    return answer


