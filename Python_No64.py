"""
10진수를 16진수로 변환하기(hex)
"""

h1= hex(97)
h2 = hex(98)
ret1 = h1 + h2
print(ret1)

a = int(h1,16)
b = int(h2,16)
ret2 = a + b
print(hex(ret2))

"""
hex()는 인자로 입력된 10진수 정수를 16진수로 변환해서 문자열로 리턴합니다.
hex()로 변환한 16진수를 덧셈이나 뺄샘을 수행하고자 하면 파이썬 내장함수 int()를 이용해 숫자로 변환하여야 함

10진수 97과 98을 16진수로 변환하고 이를 문자열로 리턴하므로 h1과 h2는 각각 0x62가 됩니다
"""