def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * int(n) 
    return answer 

print(solution("hello",3))