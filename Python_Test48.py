"""
정수 숫자를 입력받을 때마다 그 합계를 출력하는 무한 루프를 작성하되 0이 입력되면 종료하도록
"""
ans = 0

while True:
    n = int(input("숫자를 입력하세요. 0을 입력하면 종료: "))
    if n == 0:
        break
    ans += n
    print(ans)

