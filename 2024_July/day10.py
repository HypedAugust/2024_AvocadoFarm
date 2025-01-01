
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 주어질 때, 
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 
# return 하는 solution 함수를 완성해보세요.

def solution(n):
    answer = 0
    if n % 7 == 0: 
        return n // 7 
    else:
        return n // 7 + 1 

print(solution(10))

# 또는 이게 훨씬 좋은 답이다.  

def solution(n):
    return (n - 1) // 7 + 1

# 옷가게 할인받기 : 머쓱이네 옷가게는 10만 원 이상 사면 5%, 
# 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
# 구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 
# solution 함수를 완성해보세요.

def solution(i):
    if i >= 500000:  # 최대 할인율부터 확인
        return i - i * 0.2
    elif i >= 300000:
        return i - i * 0.1
    elif i >= 100000:
        return i - i * 0.05
    else:
        return i  # 할인이 적용되지 않는 경우

# 정수 배열 numbers와 정수 num1, num2가 매개변수로 주어질 때, 
# numbers의 num1번 째 인덱스부터 num2번째 인덱스까지 자른 정수 배열을 
# return 하도록 solution 함수를 완성해보세요.
# 슬라이싱 

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]