"""
배열의 두 원소 바꾸기
"""

a = [1,2,3,4,5]
b = [5,4,3,2,1]

def Change_List(a, b):
    a, b = b, a
    print(a)
    print(b)

Change_List(a,b)