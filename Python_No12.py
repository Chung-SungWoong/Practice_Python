"""
for문 개념 배우기
"""

scope = [1,2,3,4,5]

for x in scope:
    print(x)
    if x < 3:
        continue   #다음 반복문 수행


    else:
        break       # 반복문 탈출

    """
    왜 에러가 뜨지? 
    이 코드대로면 4만 출력되야하는 거 아닌가?
    """


for x in scope:
    print(x)
    if x>= 3:
        break