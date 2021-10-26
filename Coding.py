"""
2016년 1월 1일은 금요일입니다. 2016년 a월 b일은 무슨 요일일까요? 
두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요. 
요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
입니다. 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 "TUE"를 반환하세요.
"""
def solution(a, b):
    answer = ''
    num = 0
    a = a - 1
    Month = [31,29,31,30,31,30,31,31,30,31,30,31]
    if a == 0:
        answer = day(b)
        return answer
    for i in range(a):  
        num += Month[i]
        print(num)
    num += b
    print(num)
    answer = day(num)
    return answer
def day(days):
    days = days % 7
    aaa = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    return aaa[days]
print(solution(5,24))