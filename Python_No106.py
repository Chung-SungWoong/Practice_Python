"""
리스트 요소 순서를 역순으로 만들기2 (reversed)
"""

listdata = list(range(5))
ret1 = reversed(listdata)
print("원본 리스트: ",end='');print(listdata);
print("역순 리스트: ",end='');print(list(ret1))

ret2 = listdata[::-1]
print('슬라이싱 이용',end='');print(ret2)