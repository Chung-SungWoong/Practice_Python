"""
몫과 나머지 구하기(divmod)
"""

a = 11113
b = 23
ret1, ret2 = divmod(a,b)
print('<%d/%d>는 몫이 <%d>, 나머지가 <%d>입니다.'%(a,b,ret1,ret2))

#divmod()는 두개의 정수를 인자로 받아 첫번째 인자를 두번째 인자로 나눈 결과를 몫, 나머지와 같이 튜플로 리턴한다.