# 자주 쓰이는 3개 함수(Range, Map & Lambda)
# 아래와 같이 1-15까지 원소*10 결과는 문자열 리스트로 출력 하세요. 
# Range, map, lambda 사용 

# 방법 1
answer = []
for i in range(1,16):
    answer.append(str(i*10))

# 방법 2
result = list(map(lambda i: str(i * 10), range(1, 16)))
print(result)

# 방법 3 
[str(i*10) for i in range(1,16)]

# 머쓱이네 피자가게는 피자를 두 조각에서 
# 열 조각까지 원하는 조각 수로 잘라줍니다. 
# 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
# n명의 사람이 최소 한 조각 이상 
# 피자를 먹으려면 최소 몇 판의 피자를 시켜야 
# 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(slice, n):
    answer = n // slice 
    if n % slice != 0:
        answer += 1
    return answer