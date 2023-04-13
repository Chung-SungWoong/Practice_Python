def solution(name, yearning, photo):
    answer = []
    score = 0
    for i in range(len(photo)):
        score = 0
        for j in photo[i]:
            if j in name:
                index = name.index(j)
                score += yearning[index]
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))



"""
굇수분이 푼 방식
def solution(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

"""