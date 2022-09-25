"""
최솟값 만들기
두 배열 A, B 가 있을떄 두 수의 값이 가장 최솟값이 되도록 하여라
"""

def solution(A,B):
    ans = 0
    A.sort()
    B.sort()
    
    for i in range(len(A)):
        ans += A[i] * B[-1-i]
    

    return ans
