# 짝수의 합 +++
def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    return answer

print(solution(10))

# 편지 
def solution(message):
    return len(message)*2
