# 45가지 기초 문제 
# 10) 중복 제거(Remove Duplicates)

# 10-1) 중복된 원소 제거 후 출력하라 
x = ["a", 1, "b", 2, "a"]
answer = []
for i in x: 
    if i not in answer: 
        answer.append(i)


answer = []
[answer.append(i) for i in x if i not in answer]

# 또는 (순서 유지 방법) 
from collections import OrderedDict
ex1 = list(OrderedDict.fromkeys(x))

# 또는 set 
ex2 = list(set(list(x)))

# 11) Dict 합 구하기 (Dict items Sum)
# 오해 1 : Dcit과 Json(자바스크립트 오브젝트임..)은 같은건 아니다. 

d = {'a': 18, 'b' : 20, 'c' : 40}
sum_values = 0
for key in d:
    sum_values += d[key]
    

# 또는 
sum_values2 = sum([d[key] for key in d])
print(sum_values)

# 또는 
sum_values3 = sum(d.values())

# 또는 
sum_values4 = 0
for i in d.values():
    sum_values4 += i
    
# 또는 
d = {'a': 18, 'b' : 20, 'c' : 40}
sum_values5 = sum(d[item] for item in d)

#딕셔너리에서 값을 가져올 때:
#딕셔너리에서 값을 가져올 때는 대괄호 []를 사용해요: d['a']
#이것은 리스트에서 인덱스로 값을 가져오는 방식과 비슷해 보이지만, 
#딕셔너리에서는 키를 사용해요.