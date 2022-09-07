"""
로그 함수 값을 별 문자 그래프로 그리기
"""

import math 

for i in range(1,21):
    k = math.log(i) * 30             #로그 값에 적절한 숫자를 곱해 visualize 돕기
    print("%s*" %(" "*int(k)))       #k 만큼의 빈칸 후에 별모양이 나오도록   