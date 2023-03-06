A = [1,3,5,3,2,3,4,1,2,3,4,3,1,2,3,2,3,1,2,3,4,4,5,1,3,2,1,2,0]

x = [[x,A.count(x)] for x in set(A)]

print(x)

n = 0 
last = 0
answer = 0

while True:
    
    last = (x[n][1]+last)//2
    if (x[n][1]+last)%2 != 1:
        answer += 1
    n += 1


print(answer)
