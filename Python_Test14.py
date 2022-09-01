"""
0부터 100까지의 정수 5개를 입력받고, 가장 높은 점수를 출력하세요
"""

save = []
ans = []
one = save.append(int(input("0과 100사이의 정수를 입력하세요: ")))
two = save.append(int(input("0과 100사이의 정수를 입력하세요: ")))
three = save.append(int(input("0과 100사이의 정수를 입력하세요: ")))
four = save.append(int(input("0과 100사이의 정수를 입력하세요: ")))
five = save.append(int(input("0과 100사이의 정수를 입력하세요: ")))

for i in range(len(save)):
    if isinstance(save[i],int) == True:
        if 0 <= save[i] and save[i] <= 100:
            ans.append(save[i])
        else:
            continue
    else:
        continue

answer = max(ans)
print(answer)