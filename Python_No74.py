"""
1바이트에서 상위 4비트 추출하기
"""

a = 107
b = (a>>4) & 0x0f
print(b)