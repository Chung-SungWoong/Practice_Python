"""
Counter 사용법
"""

from collections import Counter

li = [2,1,2,2,4,4,6,6,3,10,1,1,2,3,5,56,32,2,4,1,6]

cnt = [[val,key] for key, val in Counter(li).items()]

print(sorted(cnt,key = lambda x: (x[0],x[1]), reverse = True))


