"""
0~9까지의 숫자 6가지 + 5중의 한개의 조
연금복권
"""

import random

print(str(random.randint(1,5)) + '조',end = '')

for i in range(6):
    print(random.randint(0,9),end = '')
print('')