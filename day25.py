# &과 and의 차이를 명확히 하자 
# 둘다 논리 연산자임! 
# &는 비트 단위 
# and는 불리언. 두 조건이 참일때 활용 

# Add Dict Items 
d1 = {'c': 'banana', 'd':'kiwi'}
d2 = {'a': 'apple', 'b': 'grape'}

d2.update(d1)
print(d2)

# python dict에서 key로 value 접근하기 -> e[key]
# dict와 update 매소드 사용하기. 

# 다른 방법 1
test1 = {'a':'apple', 'b':'grape'}
test1['c'] = 'banana'
test1['d'] = 'kiwi'
print(test1)
#{'a': 'apple', 'b': 'grape', 'c': 'banana', 'd': 'kiwi'} 

# Dict Data Filtering 
# 아래와 같은 딕셔너리 구조에서 Value 값이 25이상 
# 필터링 후 출력하세요. 

d = {'a':2, 'b':25, 'c':90, 'd': 15}

newD = {}
for key in d: 
    if d[key] >= 25:
        newD[key] = d[key]

print(newD)

# Dict 필터링의 경우 : key, value 둘다 필터링 가능 
# Filter 함수도 사용해 보기 
# Dict Comprehension으로 처리 해보기 
d = {'a':2, 'b':25, 'c':90, 'd': 15}
ex1 = {}
for k, v in d.items():
    if v >= 25:
        ex1[k] = v

print(ex1)

# 딕셔너리 컴프리핸션 
d = {'a':2, 'b':25, 'c':90, 'd': 15}
ex2 = {k:v for k, v in d.items() if v >= 25}
print(ex2)

# 람다 
d = {'a':2, 'b':25, 'c':90, 'd': 15}
ex3 = dict(filter(lambda v : v[1] >= 25, d.items()))
print(ex3)