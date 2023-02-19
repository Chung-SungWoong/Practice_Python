def solution(cards1, cards2, goal):
    answer = ''
    answer = "Yes"
    for i in range(len(goal)):
        if len(cards1) != 0 and cards1[0] == goal[i]:
            cards1.pop(0)
            pass
        elif len(cards2) != 0 and cards2[0] == goal[i]:
            cards2.pop(0)
            pass
        else:
            answer = "No"
            continue
    return answer

print(solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"]))