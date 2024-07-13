# range 함수를 복습해보자. 

#1 
#range(start, stop, step)

for i in range(1,10,2):
    print(i)

for i in range(10,0,-1):
    print(i)

# len을 복습해보자. 
# set은 중복을 len으로 세지 않는다. 

text = "abc"
for i in range(len(text)):
    print(f"index {i}: {text[i]}")

