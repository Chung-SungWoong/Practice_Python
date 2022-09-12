"""
1에서 100까지 숫자에서 3의 배수 합 (1683)을 수하여 출력하세요.
"""
ans = 0
for i in range(0,101,3):
    ans += i

print(ans)