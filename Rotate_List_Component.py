"""
배열 회전
배열 arr[]과 위치 s, t가 있을 때 arr[s] 부터 arr[t] 까지 오른쪽으로 한 칸씩 이동
"""
arr = [1,2,3,4,5,6,7]
def Rotate_List(arr, s, t):
    check = arr[t]
    for i in range(t,s,-1):
        arr[i] = arr[i-1]
    arr[s] = check
    return arr

print(Rotate_List(arr,3,6))