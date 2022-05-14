"""
리스트 요소 무작위로 섞기
"""

from random import shuffle


listdata = list(range(1,11))
for i in range(3):
    shuffle(listdata)
    print(listdata)

