"""
for문 개념 배우기 1
"""

scope = [1,2,3,4,5]
for x in scope:
    print(x)

#for문의 범위로 사용되는 것은 시퀸스 자료형 또는 반복 가능한 자료여야한다
#ex) 문자열, 리스트나 튜플, 사전, range() 등등

str = 'abcdef'
for c in str:
    print(c)

list = [1,2,3,4,5]
for d in list:
    print(d)

ascii_codes = {'a':97, 'b':98, 'c':99}
for y in ascii_codes:
    print(y)    
    #print(type(y))     ans) str

for c in range(10):
    print(c)
