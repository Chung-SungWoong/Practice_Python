"""
떡볶이 떡 만들기
The arrays are the length of the strings
Want to get the total of target length (or more) with one cut 
what is the appropriate length to cut?
"""

n, target = map(int,input().split(' '))

array = list(map(int,input().split()))

def ricecake(array,target,min,max):
    size = 0
    mid = (min + max)//2

    for i in array:
        if i > mid:
            size += (i - mid)
        else:
            pass
    if size > target:
        ricecake(array,target,mid,max)
    elif size == target:
        return mid
    else: 
        ricecake(array,target,min,mid)

print(ricecake(array,target,0,max(array)))

"""
min(array), max(array) 써야하는걸 min(array), min(array) 써놔서 디버깅 1시간 소모
제발 잔실수 줄이기
"""