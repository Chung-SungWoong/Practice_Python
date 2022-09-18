"""
converting time
"""


import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = 0
    t = ''
    if 'PM' in s:
        if s[0:2] == "12":
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
    return t[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()