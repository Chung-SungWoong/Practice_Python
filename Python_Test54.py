"""
자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
"""


# 아이디어 무거운거 두개가 같이 들어갈 수 있으면 같이 들어가고
# 두개가 들어갈 수 없을 경우에는 무거운거 하나와 가벼운거 넣어보기
n = 300

m = str(bin(n)).count('1')

while True:
    n += 1
    if str(bin(n)).count('1') == m:
        break

print(n)