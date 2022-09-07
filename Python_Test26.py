"""
0 ~ 100범위의 숫자를 입력받아 그 점수를 출력하소, 60점 미만이면 '탈락' 90점 이상은 우수를 출력하시오
"""

while True:
    score = int(input("점수를 입력하세요 (나가려면 -1 입력):  "))
    if score == -1:
        break
    elif score < 0 or score > 101:
        print("잘못된 점수입니다. 다시 입력해주세요")
    elif score < 60:
        print(score)
        print("탈락")
    elif score >= 90:
        print(score)
        print("우수")
    else:
        print(score)