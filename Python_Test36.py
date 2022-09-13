score = list(map(int,input("숫자 4개 입력 ").split(' ')))
total = sum(score)
average = total/4

if min(score) > 40 and average > 60:
    print('합격')

else:
    print('불합격')