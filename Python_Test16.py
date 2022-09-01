"""
달리기 선수가 하루에 10, 6, 9, 8, 12 km씩 달렸을 때 합계와 평균을 출력하시오.
"""
total = 0

for i in range(0,5):
    total += int(input("하루에 달린 거리: "))

average = total/5

print("달리기 선수가 달린 총 거리는 " + str(total) + "km이고 평균 거리는 " + str(average) + "km이다.")

# 숫자를 리스트안에 넣어 sum function으로 한번에 더할수있다.