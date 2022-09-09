"""
재귀 함수를 이용한 fibonachi 수열
"""
"""
def fibo(x):
	if x == 1 or x == 2:
		return 1
	return fibo(x - 1) + fibo(x -2)

print(fibo(4))
"""

#n 이 커질수록 필요 계산식이 많아져 시간이 오래 걸린다

# 메모이제이션 기법을 사용한 피보나치 수열

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x -2)
    return d[x]

print(fibo(99))

#바텀 업 방식을 사용하였을 때의 피보나치 수열 알고리즘

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3,n+1):
	d[i] = d[i - 1] + d[i -2]

print(d[n])

