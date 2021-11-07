"""
정수 n 이하의 모든 소수 구하기
"""

def getPrime(n):
    ret = [2]
    if n <= 2:
        return ret
    
    for i in range(3,n + 1, 2):
        for k in range(3,int(i/2),2):
            a = i%k
            if a ==0:
                break
    
        else:
            ret.append(i)
    
    return ret

ret = getPrime(10)
print(ret)
