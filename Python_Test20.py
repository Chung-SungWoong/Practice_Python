"""
1~45사이의 로또번호 6개씩 5번 출력하세요
로또 생성기
"""

import random

numbers = []
ans = []

while True:
    if len(ans) == 6:
        break
    numbers.append(random.randint(1,45))
    ans = [*set(numbers)]

ans = sorted(ans)
print(ans)
