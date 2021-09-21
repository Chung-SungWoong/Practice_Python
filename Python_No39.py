"""
함수 이해하기 (def)
"""

def add_number(n1,n2):
    ret = n1 + n2
    return ret

def add_tx(t1,t2):
    print(t1,t2)

ans = add_number(10,15)
print(ans)

txt1 = '대한민국~'
txt2 = '만세!!'
add_tx(txt1,txt2)

"""
인자와 리턴값이 있는 함수
def 함수이름(인자1,인자2):
    코드들
    return 결과값               #변수 = 함수이름(값1,값2)

인자 x 리턴 o
def 함수이름():
    코드들
    return 결과값               #함수이름(값1,값2)

인자x 리턴 x 
def 함수이름():
    코드들
    return (또는 생략)          #함수이름()
"""