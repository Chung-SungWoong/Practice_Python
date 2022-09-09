"""
1로 만들기
정수 x가 주어질 때 정수 x에 사용할 수 있는 연산은 다음과 같이 4가지이다
a. x가 5로 나누어떨어지면 5로 나눈다
b. x가 3으로 나누어떨어지면 3으로 나눈다
c. x가 2로 나누어떨어지면 2로 나눈다
d. x에서 1을 뺀다

연산을 사용하는 횟수의 최솟값을 출력하시요
"""
"""
d = [0] * 300


def makeone(x):
    count = 0
    y = x
    while y != 1:
        if d[y] != 0:
            return d[y]
        elif y % 5 == 0:
            y = y//5
            count += 1
        elif y % 3 == 0:
            y = y//3
            count += 1
        elif y % 2 == 0:
            y = y//2
            count += 1
        else:
            y = y - 1
            count += 1

    d[x] = count + d[y]
    return d[x]

print(makeone(26))
"""
"""
에러 이유: 순번대로 진행하는 것이 아닌 최솟값을 찾는 문제였음
밑에 코드가 모범 답안
"""

x = int(input())

d = [0] * 30001

for i in range(2, x+ 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i],d[i//2] +1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if  i % 5 == 0:
        d[i] == min(d[i],d[i//5] + 1)

print(d[x])