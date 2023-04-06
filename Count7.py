def solution(array):
    answer = 0
    for i in array:
        if str(i).count('7'):
            answer += 1

    return answer

print(solution([7, 77, 17]))