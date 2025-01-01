# 최댓값 만들기 
# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 
# return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    # 가장 큰 숫자를 찾고 리스트에서 제거해요.
    first_max = max(numbers)
    numbers.remove(first_max)
    
    # 두 번째로 큰 숫자를 찾아요.
    second_max = max(numbers)
    
    # 두 숫자를 곱해서 반환해요.
    return first_max * second_max

# 예시 실행
numbers = [1, 2, 3, 4, 5]
print(solution(numbers))  # 출력: 20 (4 * 5)

# 리스트 컴프리핸션을 공부해보자! 
# 루프 이해하기 
numbers = []
for i in range(1,5):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(1,6)]
print(numbers)

even_numbers = [i for i in range(1,11) if i % 2 == 0]

squared_numbers = [i**2 for i in range(1,6)]

numbers = [i if i % 2 != 0 else i*2 for i in range(1,11)]