# 짝수 홀수 개수
def solution(num_list): 
    sum_i = 0
    sum_j = 0
    for i in num_list: 
        if i % 2 == 0:
            sum_i += 1
    for j in num_list:
        if j % 2 != 0:
            sum_j += 1
    return (sum_i,sum_j)

print(solution([1,2,3,4,5]))

# 다른 방법 
def solution(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    return answer

# 각도기 
def solution(angle):
    if 0 < angle < 90: 
        return 1
    elif angle == 90:
        return 2
    elif 90 < angle < 180:
        return 3
    elif angle == 180:
        return 4
        
print(solution(70))
         
