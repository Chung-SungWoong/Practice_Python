"""
2~8자리 양의 정수를 입력받고 각 자리의 수를 반대로 출력하세요.
예) 12345 -> 54321
"""
# 내가 해본 것
n = list(input())

n.reverse()
ans = ''
for i in n:
    ans += i
ans = int(ans)
print(ans)
"""
옳은 답 1
"""

num = -1
num2 = 0

while num < 10 or num > 99999999:
    num = int(input("2~8자리 양의 정수를 입력하세요: "))

while num > 0:
    num2 *= 10
    num2 += int(num%10)
    num = int(num/10)
print("뒤집힌 숫자: %i" %int(num2))

"""
옳은 답2
"""

num = -1

while num < 10 or num > 99999999:
    num = int(input("2~8자리 양의 정수를 입력하세요: "))

str = ''.join(reversed(str(num)))
print(str)
