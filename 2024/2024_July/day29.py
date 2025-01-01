# 최댓값 만들기 
# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 
# 최댓값을 return하도록 solution 함수를 완성해주세요.

# def solution(numbers):
#     for i , j in numbers: #단일값은.. 이렇게 못씀. 
#         return max(i)*max(j)  

# def solution(numbers):
#     sorted_numbers = sorted(numbers, reverse = True)
#     return sorted_numbers[0]*sorted_numbers[1]
#  # 음수끼리 곱함은 안됨. 

def solution(numbers):
    i = i(numbers, reverse = True)
    return max(i[0]*i[1],i[-1]*i[-2])