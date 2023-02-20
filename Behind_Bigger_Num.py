def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        if i == len(numbers) or max(numbers[i+1:]) < numbers[i]:
            answer.append(-1)
        else:
            for n in range(i,len(numbers)):
                if numbers[n] > numbers[i]:
                    answer.append(numbers[n])
                    break
                else:
                    continue
    answer.append(-1)
    return answer

print(solution([9, 1, 5, 3, 6, 2]))