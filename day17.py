# "*"의 높이와 너비를 1이라고 했을 때, "*"을 이용해 
# 직각 이등변 삼각형을 그리려고합니다. 
# 정수 n 이 주어지면 높이와 너비가 n 인 
# 직각 이등변 삼각형을 출력하도록 코드를 작성해보세요.

n = int(input())
for i in range(1,n+1):
    print('*'*i)
    
# 2-1 Assigning & Comparison 
# 불필요한 객체 형성 방지 = 메모리 절약 / 사이드 이펙트 예방 

x = 15 
y = 25 

print(f'x == y : {x == y}')
print(f'x is y : {x is y}')

# array 라고 하는걸 파이썬에선 list라고 함 

x = ['orange', 'apple']
y = x 
print(f'x == y : {x == y}') # 그치만 값도 같다. 
print(f'x is y : {x is y}') # 이게 정답. 객체가 같으니까. 값이 아니구. 

# 증명 방법 
print(f'x value, id : {x}, {hex(id(x))}')
print(f'x value, id : {y}, {hex(id(y))}')

# 예제 3 
# 잘했다! 
x = ['orange', 'apple']
y = ['orange', 'apple'] 
print(f'x == y : {x == y}') # true
print(f'x is y : {x is y}') # false

# 중요한 점은 값이 같다는게 객체가 같다는 것과 다르다. 
# hex 쳤을 때 주소값이 다르기 떄문이다. 

# 기억하기 
# is, not is -> 객체 비교 
# ==, != 

# 선분 세 개로 삼각형을 만들기 
# 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 
# 작아야 합니다.
# 삼각형의 세 변의 길이가 담긴 배열 sides이 
# 매개변수로 주어집니다. 세 변으로 삼각형을 만들 수 있다면 1, 
# 만들 수 없다면 2를 return하도록 solution 함수를 완성해주세요.

def solution(sides):
    longest = max(sides)
    sumofothers = sum(sides) - longest
    if longest < sumofothers:
        return 1
    else:
        return 2
    
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2

# 문자열 my_string과 정수 num1, num2가 
# 매개변수로 주어질 때, my_string에서 인덱스 num1과 
# 인덱스 num2에 해당하는 문자를 바꾼 
# 문자열을 return 하도록 solution 함수를 완성해보세요.

# string([4])

def solution(my_string, num1, num2):
    # 문자열을 리스트로 변환합니다.
    string_list = list(my_string)
    
    # num1과 num2 위치의 문자를 바꿉니다.
    string_list[num1], string_list[num2] = string_list[num2], string_list[num1]
    
    # 리스트를 다시 문자열로 변환합니다.
    return ''.join(string_list)