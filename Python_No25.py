"""
비트 연산자 이해하기 (&,|,~,^,>>,<<)
"""

bit1 = 0x61
bit2 = 0x62

print(hex(bit1 & bit2))     
print(hex(bit1 | bit2))
print(hex(bit1 ^ bit2))
print(hex(bit1 >> 1))
print(hex(bit1 << 2))

"""
A & B = A와 B의 비트간 and 연산을 수행
A | B = A와 B의 비트간 or 연산을 수행
A ^ B = A와 B의 비트간 배타전 논리합 (xor) 수행
~A = A의 비트를 반전시킴
A >> n = A의 모든 비트를 n만큼 오른쪽으로 시프트 시킴
A << n = A의 모든 비트를 n만큼 왼쪽으로 시프트 시킴
"""