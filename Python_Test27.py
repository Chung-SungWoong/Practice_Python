s = "-1 -2 -3 -4"

def solution(s):
    answer = ''
    temp = []
    num = []
    blank = []
    for i in range(len(s)):
        temp.append(s[i])
    
    for i in range(len(temp)):
        if temp[i] == ' ':
            blank.append(i)

    for i in range(len(blank)+1):
        if i == 0:
            if temp[i] == '-':
                num.append(-abs(int("".join(map(str,temp[1:blank[i]])))))
            else:
                num.append(int("".join(map(temp[:blank[i]]))))
        if i == len(blank) + 1:
            if temp[blank[i-1]+1] == '-':
                num.append(-abs(int("".join(map(temp[blank[i-1] + 2:])))))
            else:
                num.append(int("".join(map(temp[blank[i-1] + 1:]))))

        else:
            if temp[blank[i-1]+1] == '-':
                num.append(-abs(int("".join(map(temp[blank[i-1]+2:blank[i]])))))
            else:
                num.append(int("".join(map(temp[blank[i-1]+1:blank[i]]))))
                       
    answer = str(min(num)) + ' ' + str(max(num))
    return answer

print(solution(s))