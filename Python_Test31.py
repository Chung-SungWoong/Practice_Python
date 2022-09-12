"""
0에서 100까지 숫자에서 짝수 합을 구하여 출려하세요
"""

ans = 0

for i in range(101):
    if i % 2 == 0:
        ans += i

print(ans)