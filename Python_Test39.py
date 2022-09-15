"""
2~8자리 양의 정수를 입력받고, 각 자리의 수를 반대로 출력하세요.
예를 들어, '12345'를 입력하면 '54321'을 출력합니다.
"""

num = input(("2~8자리의 양의 정수를 입력하세요: "))
ans = []

if 2 <= len(num) and len(num) <= 8:
    for i in range(1,len(num)+1):
        ans.append(num[-i])
    result = ''.join(ans)
    print(result)
else:
    print("잘못된 입력값입니다. ")