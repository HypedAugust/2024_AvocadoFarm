# 짝수는 싫어요. 
# 정수 n이 매개변수로 주어질 때, 
# n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 
# solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 != 0:
            answer.append(i)
    return answer

# 자릿수 더하기 
# 정수 n이 매개변수로 주어질 때 
# n의 각 자리 숫자의 합을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    new = str(n)
    add = 0 
    for i in range(len(new)):
        add += int(new[i])
    return add

# 아이스 아메리카노 
# 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 
# 아이스 아메리카노는 한잔에 5,500원입니다. 
# 머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때, 
# 머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 
# 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(money):
    x = money // 5500 
    y = money % 5500 
    answer = [x, y]
    return answer