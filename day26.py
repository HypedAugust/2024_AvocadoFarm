# 딕셔너리 컴프리핸션을 복습해보자!
# {key expression : value expression for itme in iterable}
# 리스트, 튜플, 기존 딕셔너리 기반으로 한다. 
numbers = [1,2,3,4,5]
squared_dict = {i:i**2 for i in numbers if i % 2 == 0}
print(squared_dict)

 
# 람다 함수를 복습해 보자! 
# 람다 함수 = 이름이 없이 정의 되는 간단한 함수 
# lambda arguments : expression 
add = lambda x, y : x + y
print(add(2,3))

# 람다 함수는 간단한 연산, 일회성 함수때 쓰며, map, filter와 
# 같은 고차 함수와 사용된다. 

numbers = [1,2,3]
squared = list(map(lambda x: x**2, numbers ))