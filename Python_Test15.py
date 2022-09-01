"""
다섯개 정수 숫자를 입력받고 가장 큰 수와 가장 작은 수를 출력하세요
"""


save = []
ans = []

for i in range(0,5):
    save.append(int(input("0과 100사이의 정수를 입력하세요: ")))

print("가장 높은 점수는: " + str(max(save)) + "\n가장 낮은 점수는: " + str(min(save)))
