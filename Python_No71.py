"""
정수 리스트에서 소수만 걸러내기
"""

def getPrime(x):
    if x%2 == 0:
        return

    for i in range(3,int(x/2),2):
        if x%i ==0:
            break
    
    else:
        return x

listdata = [1,2,3,4,5,6,7,8,9,10]
ret = filter(getPrime,listdata)
print(list(ret))

#filter는 리스트와 같이 반복 가능한 자료에서 특정 조건을 만족하는 값만을 추출할 수 있는 방법을 제공
