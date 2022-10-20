"""
두 변수의 값 바꾸기

"""

def change_val(a,b):
    a, b = b, a
    return a,b

print(change_val(2,5))