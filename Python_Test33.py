"""
500원짜리 빵을 10개 샀을 때 가격을 구하세요. 단, 10개 사면 15% 깎아줍니다.
"""

bread = 500
n = 10

if n == 10:
    bread = 500 * 0.85

price = int(bread * n)

print("빵 10개의 가격은 %i 입니다."%price) 