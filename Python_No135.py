"""
이름없는 한줄짜리 함수 만들기
"""

add = lambda x,y:x+y
ret = add(1,3)

print(ret)

focus = [lambda x:x +'.pptx', lambda x:x + '.docx']
ret1 = focus[0]('intro')
ret2 = focus[1]('Report')
print(ret1)
print(ret2)

names = {'Marry':10999,'Sams':2111,'Aimy':9778,'Tom':20245,'Michale':27115,'Bob':5887,'Kelly':7855}
ret3 = sorted(names.items(),key=lambda x:x[0])
print(ret3)