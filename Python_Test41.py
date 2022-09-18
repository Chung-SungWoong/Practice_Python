"""
비밀지도
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다."""

def solution(n, arr1, arr2):
    answer = []
    line = ""

    arr_bi1 = [str(format(x,'b')).zfill(n) for x in arr1]
    arr_bi2 = [str(format(x,'b')).zfill(n) for x in arr2]

    for i in range(n):
        for j in range(n):
            if arr_bi1[i][j] == '1' or arr_bi2[i][j] == '1':
                line += "#"
            else:
                line += " "
        answer.append(line)
        line = ""
    return answer

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))