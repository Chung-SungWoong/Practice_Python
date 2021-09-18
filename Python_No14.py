"""
while문 개념 배우기
"""

x = 0
while x < 10:
    x = x + 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break 

"""
while 조건:
    반복 코드 실행
    continue        # while문의 처음으로 이동하여 반복문 계속

    ...

    break           # while문 탈출
 while문은 특정 조건을 만족할 때까지 반복 실행하는 무한 루프를 구현하는 경우에 많이 사용됨
"""
y = 1
total = 0
while 1:
    total = total + y
    if total > 100000:
        print(y)
        print(total)
        break
    y = y + 1