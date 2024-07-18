# sequence type indexing 
# 인덱싱 이라는건 추출하라는 거다. 

x = ["banana", 'apple', 'carrot']
print(x[x.index('banana')])
#print(x[1]) 
#print(x.index("banana"))

# 시퀀스 자료형 : list, tuple, str, range .. 
# list 관련 함수는 중요!
# cmp, lwn, max, min, list, append, count, extend, index, insert
# pop, remove, reverse, sort 등등

# index 함수 대소문자 구분 
# sort, sorted 함수 차이를 알 것. 

print('banana'in x)
print(x[x.index('banana')],0,len(x))