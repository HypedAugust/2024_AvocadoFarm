# 프로그래머스 
# 피자를 여섯 조각으로 잘라 줌
# 피자를 나눠먹을 사람의 수 n임  
# 조건1) n명이 주문한 피자를 남기지 않고 
# 조건2) 모두 같은 수의 피자 조각을 먹어야 한다면 
# 최소 몇 판을 시켜야 하는지?

import math

def solution(n):
    answer = 0
    a = 6
    answer = int((math.lcm(a,n))/6)
    return answer

print(solution(3))

def solution(n):
    for i in range(1, n+1):
        if (6 * i) % n == 0:
            return i
        
answer = [i for i in range(1, n+1) if (6 * i) % n == 0]