"""
문자열 빈칸에 따라 나눠보기
그리고 순서를 바꿔보기
"""

letter = "Hi Im Chung Sung Woong"

ans = letter.split(' ')
num = len(ans) // 2

for i in range(num):
    ans[i], ans[-i-1] = ans[-i-1], ans[i]

print(ans)
