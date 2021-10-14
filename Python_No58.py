"""
예외처리 이해하기 4
try~except Exception as e
"""
try:
    print(param)
except Exception as e:
    print(e)        #name 'param' is not defined

"""
예제에서는 param이라는 정의되지 않은 변수를 코드에서 쓰고 있고 이는 파이썬에서 예외를 발생시키고
except Exception as e는 NameError 객체를 e라는 이름으로 접근할 수 있게 해준다.
line 8에서는 NameError 객체를 출력한 결과이다
"""