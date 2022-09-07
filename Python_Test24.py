"""
Finding the items
"""
"""
for test
"""
have = [4, 9, 13, 6, 1, 3, 16]
want = [5,4,2,13]
n = 7
m = 4
answer = []

"""
have = []
want = []
answer = []
n = int(input())
have = list(map(int,input().split()))
m = int(input())
want = list(map(int,input().split()))

"""
have = sorted(have)

def binary(array, target, start, end):
    mid = (start + end)//2
    print(mid)
    if start > end:
        answer.append("No")
        return None
    elif array[mid] == target:
        answer.append("yes")
        return 

    elif target <= array[mid]:
        return binary(array, target ,start, mid - 1)

    else:
        return binary(array, target ,mid + 1, end)

for i in want:
    binary(have, i, 0, len(have)-1)

print(answer)