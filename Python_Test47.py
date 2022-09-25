"""
도서관에서 책을 빌린 후 3일 안에 반납하지 않으면 1일당 150원씩 과태료가 부과됩니다
단 30일 후에 반납될 때는 100원씩 추가 과태료를 내야 합니다 
책을 빌리고 45일 후 반납했다면 과태료는 얼마인지 출력하세요
"""

n = 3
ans = 0
day = 1
while True:
    if day < 30:
        price = 150
        ans += price
    
    elif day >= 30:
        price = 250
        ans += price

    day += 1
    if day == 45:
        break

ans = ans * n
print("연체료는 ", str(ans), "입니다")