"""
10진수 12586을 16진수 값 '312A'처럼 출력하세요.
단 hex 함수를 사용하지 말고
"""

from queue import deque

li = deque()

num = int(input("16진법으로 바꿀 숫자를 입력하세요"))
t = 0

while True:
    if num < 16:
        li.appendleft(num)
        break
    t = num % 16
    num //= 16
    if t >= 10:
        t += 55
        li.appendleft(chr(t))
    else:
        li.appendleft(t)

str = ''.join(map(str,li))

print("%d를 16진법으로 표현하면 %s 입니다." %(num,str))