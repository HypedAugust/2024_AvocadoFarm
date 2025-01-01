# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 
# 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([(i, n//i)])
    return len(answer) 

def solution(n):
    return len([number for number in range(1,n+1) if n % number == 0])

# 짝수 싫어요. 
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i //2 == 1:
            answer.append(i)
    return answer

# len에는 숫자를 못씁니다. 

# 순서쌍 : 약수의 갯수는 순서쌍의 갯수와 같아요! 
def solution(n):
    answer = []
    for i in range(1,n+1):
        if n % i == 0:
            answer.extend([i,n//i])
    return len(answer)

def solution(n):
    return len([number for number in range(1,n+1) if n % number ==0])


# extend에 대해서 알아보자. 

emotion1 = ["슬픔"]
emotion2 = ["기쁨"]
emotion1.extend(emotion2)
print(emotion1)

# 리스트 컴프리핸션에 대해 알아보자 
even_doubles = [num*2 for num in range(1,11) if num % 2 == 0]
print(even_doubles)

numbers = [num for num in range(1,6)]
print(numbers)

even_numbers = [num for num in range(1,11) if num % 2 == 0]
print(even_numbers)

# 1 부터 5 까지 숫자의 제곱 리스트 만들기 
squares = [ num**2 for num in range(1,6)]
print(squares)

# 문자열 다루기 (이해가 안됨)
word = "hello"
upper_letters = [letter.upper() for letter in word]
print(upper_letters)

# 풀어서 쓰기 
word = "hello"
upper_letters = []
for letter in word:
    upper_letters.append(letter.upper())
print(upper_letters)

# 중첩 리스트 만들기 (이해가 안됨)
matrix = [[i*3+j] for j in range(3) for i in range(2)]
print(matrix)

# 풀어서 쓰기 
matrix = []
for i in range(2):
    row = []
    for j in range(3):
        row.append(1*3 + j)
    matrix.append(row)
print(matrix)

# 딕셔너리 컴프리핸션 
square_dict = {num: num**2 for num in range(1,6)}
print(square_dict)

# 개미 군단이 사냥을 나가려고 합니다. 
# 개미군단은 사냥감의 체력에 딱 맞는 병력을 데리고 나가려고 합니다. 
# 장군개미는 5의 공격력을, 병정개미는 3의 공격력을 일개미는 1의 공격력을 가지고 있습니다. 
# 예를 들어 체력 23의 여치를 사냥하려고 할 때, 일개미 23마리를 데리고 가도 되지만, 
# 장군개미 네 마리와 병정개미 한 마리를 데리고 간다면 더 적은 병력으로 사냥할 수 있습니다. 
# 사냥감의 체력 hp가 매개변수로 주어질 때, 사냥감의 체력에 딱 맞게 최소한의 병력을 구성하려면 
# 몇 마리의 개미가 필요한지를 return하도록 solution 함수를 완성해주세요.


#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

def solution(hp):
    general = 5
    soldier = 3
    worker = 1

    ant_count = 1

    # 장군개미 
    ant_count += hp // general 
    hp = hp % general 

    # 병정개미
    ant_count += hp // soldier
    hp = hp % soldier

    # 일개미
    ant_count += hp # 남은 hp는 모두 일개미로 처리 

    return ant_count

def solution(hp):
    return hp // 5 + (hp % 5) // 3 + (hp % 5) % 3

# 모음 제거 
# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
# 문자열 my_string이 매개변수로 주어질 때 
# 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    vowels = 'aeiou'
    answer = ''
    for char in my_string:
        if char.lower() not in vowels:
            answer += char
    return answer 

def solution(my_string):
    return ''.join([char for char in my_string if char.lower() not in 'aeiou'])

# 숨어있는 숫자의 덧셈(1)
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 return하도록 
# solution 함수를 완성해주세요.

# 내답 : 모듈을 쓰는건 과감했으나, 메모리 사용이 크다. 
import re
def solution(my_string):
    numbers = re.findall(r'\d', my_string)
    return sum(int(num) for num in numbers)

# 좋은 답 : 메모리 사용이 적고 짧고 파이썬답다. 
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

