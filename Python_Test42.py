"""
Plus and Minus
"""


import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    answer = []
    for i in range(len(arr)):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zero += 1
    print(format(pos/len(arr),'.6f'))
    print(format(neg/len(arr),'.6f'))
    print(format(zero/len(arr),'.6f'))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)


