"""
1부터 10의 4제곱 값을 pow()함수로 계산하여 출력하고 그 결과들의 합을 출력하세요
"""

total = 0 
for i in range(1,10):
    print(str(i) + "의 4제곱은 " + str(pow(i,4)))
    total += pow(i,4)

print(total)