"""
사칙 연사자 이해하기
"""

a = 2
b = 4
ret1 = a + b
ret2 = a - b
ret3 = a * b
ret4 = a / b
ret5 = a ** b
ret6 = a + a *b / a
ret7 = (a+b) + (a-b)
ret8 = a * b ** a

#만약 For loop 하나로 ret1 부터 ret8까지 프린트 하고 싶으면 어떻게 해야하지???

array1 = []
tem = 0

for i in range(8):
    tem = i+1
    array1.append(chr(tem))
    print("ret"+array1[i])

    #??? 실패
