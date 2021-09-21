"""
함수 인자 이해하기
"""


def add_txt(t1, t2='파이썬'):
    print(t1 + ':' + t2)


add_txt('베스트')
add_txt(t2='대한민국', t1='1등')


def func1(*args):
    print(args)


def func2(width, height, **kwargs):
    print(kwargs)


func1()  # 빈 튜플이 () 출력됨
func1(3, 5, 1, 5)  # (3,5,1,5)가 출력됨
func2(10, 20)  # 빈 사전 {}이 출력됨
func2(10, 20, depth=50, color='blue')  # {'depth':50,'color':'blue'}가 출력됨

"""
인자의 개수가 불명확한 경우 가변인자를 활용하여 함수를 선언
*args는 튜플로 처리

마찬가지로 키워드 인자가 불명확한 경우는 **kwargs를 사용
내부적으로 사전으로 처리
"""
