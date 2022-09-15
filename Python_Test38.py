"""
서로 다른 수를 세 개 입력받고, 크기가 중간인 수를 출력하세요.
만약 같은 수를 입력받으면 다시 입력하세요
"""
num = []

while len(num) < 4:
    num = list(map(int,input("숫자 3개를 입력하세요: ").split(" ")))
    break
num = sorted(num)

print(num[1])