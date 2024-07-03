# 최빈값 구하기
# 정수 , array, 최빈 값 return, 1개 이상 최빈값 = -1 
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

# 짝수는 싫어요. 
def solution(n):
    return[i for i in range(1, n+1, 2)]
