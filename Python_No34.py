"""
문자열 포맷팅 이해하기
"""
from time import sleep


txt1 = '자바'; txt2 = '파이썬'
num1 = 5; num2 = 10
print('나는 %s보다 %s에 더 익숙합니다'%(txt1,txt2))
print('%s은 %s보다 %d배 더 쉽습니다.'%(txt2,txt1,num1))
print('%d + %d = %d'%(num1,num2,num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.'%num1)

"""
문자열 포멧팅이란 변하는 값을 포함하는 문자열을 표현하기 위한 하나의 양식
%s = 문자열에 대응
%c = 문자나 기호 한 개에 대응
%f = 실수에 대응
%d = 정수에 대응
%% = %라는 기호를 표시함
"""

for i in range(100):
    msg = '\r진행률 %d%%'%(i+1)
    print(''*len(msg),end='')
    print(msg,end='')
    sleep = 0.1