"""
파이썬 모듈 이해하기
"""

import time

print('5초간 프로그램을 정지합니다')
time.sleep(5)
print("5초가 지나갔습니다")

import mylib

ret1 = mylib.add_txt('대한민국','1등')
ret2 = mylib.reverse(1,2,3)
print(ret1)
print(ret2)