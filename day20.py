# 주사위의 갯수 
# 머쓱이는 직육면체 모양의 상자를 하나 가지고 있는데 
# 이 상자에 정육면체 모양의 주사위를 최대한 많이 채우고 싶습니다. 
# 상자의 가로, 세로, 높이가 저장되어있는 배열 box와 주사위 모서리의 길이 
# 정수 n이 매개변수로 주어졌을 때, 상자에 들어갈 수 있는 주사위의 최대 개수를
#  return 하도록 solution 함수를 완성해주세요.

def solution(box, n):
    answer = 0
    answer = (box[0] // n)*(box[1] // n)*(box[2]//n)
    return answer

# 문자열 str1, str2가 매개변수로 주어집니다. 
# str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(str1, str2):
    if str2 in str1:
        return 1
    else:
        return 2
    
def solution(str1, str2):
    return 1 if str2 in str1 else 2

# 어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 
# 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 
# 세균의 수를 return하도록 solution 함수를 완성해주세요.
def solution(n,t):
    return n * (2 ** t)

def solution(n,t):
    return n << t

# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
# 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 
# 아니라면 2를 return하도록 solution 함수를 완성해주세요.

import math 
def solution(n):
    sqrt_n = math.sqrt(n)
    int_sqrt_n = int(sqrt_n)
    if int_sqrt_n ** 2 == n:
        return 1
    else:
        return 2
    
def solution(n):
    if n**(1/2) == int(n**(1/2)):
        return 1
    else:
        return 2
   


