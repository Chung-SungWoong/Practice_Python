"""
두 실수 x, y를 입력받아 root x^2 + y^2 수식을 계산한 결과를 출력하시오
"""
import math

x = float(input("x값을 입력하세요: "))
y = float(input("y값을 입력하세요: "))
ans = '{:.3f}'.format(math.sqrt(pow(x,2)+pow(y,2)))
print(ans)