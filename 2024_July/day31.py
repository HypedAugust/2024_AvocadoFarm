# def test():
#     x = 100
#     x = x * 10
#     return x

# result = test()
# print(result)  # 출력: 100

# x = 100

# def test1():
#     return x*10

# print(test1())

# y = 100
# def test2():
#     global y 
#     y *= 10
#     return y

# print(test2())

a = 20 # 전역변수 
def test():
    global a # 전역변수 쓴단 얘기임. 
    print('{a}') # 20  나옴 
    a = 35 # 전역 변수 a의 값을 35로 변경
    return a # 35 나옴 

print(a) # 20 나올 예정 

a = 100
print(a) # 100 나올 예정 
print(test()) # 100 나올 예정 


