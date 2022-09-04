"""
exchange elements between two list
make first list to have max sum
n = length of the list
k = possible chance to exchange
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)
b = list(map(int, input().split()))
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
print(sum(a))