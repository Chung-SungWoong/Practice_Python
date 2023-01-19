"""
숫자 맞추기 게임 
1 부터 100까지의 임의의 수를 생성하고 내가 수를 입력하면 그 숫자가 up or down을 알려줘서 몇번만에 맞추는지 점수를 얻는 게임
"""

# 책 없이 도전
import random

def Rand_Game():
    Try = 0
    n = random.randint(0,100)
    while True:
        try:
            m = int(input("100 이하의 숫자를 입력하세요: "))
        except:
            print("숫자가 아닙니다")
            Try = 0
            break
        Try += 1
        if m == n:
            break
        elif m < n:
            print("Up")
        else:
            print("Down")

    return str(Try) + "점" 

print(Rand_Game())

# 책에 있는 코드

random_number = random.randint(1,100)

game_count = 1
while True:
    try:
        my_number = int(input('1 ~ 100 사이의 숫자를 입력하세요: '))

        if my_number > random_number:
            print('다운')
        elif my_number < random_number:
            print('업')
        elif my_number == random_number:
            print(f" 축하합니다.{game_count}회 만에 맞췄습니다.")
            break
        game_count = game_count + 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요 ")

"""
생각보다 코드가 비슷해서 뿌듯.
물론 내가 def를 사용해서 그런것도 있지만 내 코드가 좀 더 너저분함을 느낌
"""