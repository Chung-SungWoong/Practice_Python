"""
문자열 빈칸에 따라 나눠보기
그리고 순서를 바꿔보기
"""
import math
import os
import random
import re
import sys

letter = "Hi Im Chung Sung Woong"

ans = letter.split(' ')
num = len(ans) // 2

for i in range(num):
    ans[i], ans[-i-1] = ans[-i-1], ans[i]

print(ans)


let = "12"
print(let[0:1])



def timeConversion(s):
    # Write your code here
    time = 0
    t = ''
    if 'PM' in s:
        if s[0:2] == '12':
            t = s
        else:
            time = int(s[0:2]) +12
            t += str(format(time, '02'))
            t += s[2:]
    else:
        if s[0:2] == '12':
            t += '00'
            t += s[2:]
        else:
            t = s
    print(t[:-2])
    return t[:-2]

if __name__ == '__main__':

    result = timeConversion("12:45:54PM")
   
