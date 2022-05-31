"""
인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)
"""

f = lambda x: x*x
args = [1,2,3,4,5]
ret = map(f,args)
print(list(ret))