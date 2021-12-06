"""
문자열에서 특정 문자(열) 위치 찾기 (find)
"""

txt = 'A lot of things occur each day, every day'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day',30)

print(offset1)
print(offset2)
print(offset3)