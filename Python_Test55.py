"""
people을 내림차순으로 정렬한 후에 무거운 사람부터 새 보트에 집어넣습니다. limit/2보다 초과하는 사람은 다 넣어요.(어차피 이들끼리는 같이 보트를 탈 수 없기때문)
그리고나서 남은 사람들 중 가장 무거운 사람과 마지막 보트만 체크합니다. 왜냐하면 현재 있는 타고 있는 보트 중에서 마지막에 집어넣은 보트가 가장 여유가 클 것이기 때문에 거기에 못들어가면 어차피 다른 보트에도 못 들어가요. limit보다 작다면 그 보트에 넣어주면 됩니다.

이렇게 구현하니까 반복문 딱 2번만 돌고 효율성 통과했습니다!
"""

def solution(people, limit):
    people.sort()
    check = 0
    answer = 1

    for i in people:
        if check + i <= limit:
            check += i

        else:
            answer += 1
            check = 0
            check += i

    return answer

print(solution([70, 80, 50],100))