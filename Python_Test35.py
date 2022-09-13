import random


while True:
    x = random.randint(1,100)
    y = random.randint(1,100)

    print(x, ' + ' , y , " = ")
    z = int(input())

    if z != x + y:
        print("틀렸습니다")
        break
    else:
        print("잘했어요")