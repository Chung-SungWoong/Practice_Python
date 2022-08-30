"""
정수 숫자 x를 입력받아서 (x-1)의 세제곱 값을 출력하세요. 단, 0보다 적은 값이 입력되면 다시 입력하세요.
"""

x = int(input("양수인 정수를 입력하세요: "))
while True:
    if (x > 0):
        ans = (x-1)**3
        print(ans)
        break
    else:
        x = input("숫자를 다시 기입하세요.: ") 