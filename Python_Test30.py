"""
숫자를 입력받고 정수이면 "정수입니다.", 실수이면 "실수입니다." 를 출력하세요.
단, -9999가 입력되면 종료하세요
"""

while True:
    n = input("숫자를 입력하세요: ")
    if '.' in n:
        print("실수입니다.")
    elif n == '-9999':
        break
    else:
        print("정수입니다.")
"""
모범 답안
"""

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    num = input("정수 또는 실수를 입력하세요: ")
    if isNumber(num) == False:
        continue
    num = float(num)
    num2 = int(num)

    if num2 == -9999:
        break
    elif num - num2 == 0.0:
        print("정수입니다.")
    else:
        print("실수입니다.")