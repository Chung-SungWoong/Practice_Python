"""
리스트 컴프리헨션 사용해보기
"""

test = [1,2,3,4,5,6,7,8,9,10]

lc = [i * 2 for i in test if i % 2 == 0]
print(lc)