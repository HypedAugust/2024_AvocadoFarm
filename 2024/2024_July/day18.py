# error handling 
# 연산을 할 때 자료형을 신경써야 함 
# 연습 예제 1 : 에러의 이유 

x = "seoul"
y = 25
# z = x + str(y)  # 문자열과 숫자를 연결하기 위해 숫자를 문자열로 변환
pass
print(f'x+y: {z}')  # f-string을 사용하여 z의 값을 문자열 내에 포함

# type error를 수정하는 연습! 
# type casting = 형변환을 할줄 알아야 한다. 

# 다양한 에러들 
# 형변환, calling a non callable, 리스트 인덱스 타입 에러, 기타 타입에러 

# calling a non callable 
etc = "k"
print(etc)
print(etc())

# 인덱스 타입 에러 : 슬라이스 형태나 인티저로 불러와야함. 
c = [1,2,3,4,5]
print(c[2])
print(c['2'])
print(c[1:2])