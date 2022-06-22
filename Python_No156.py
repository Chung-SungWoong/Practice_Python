"""
파일인지 디렉터리인지 확인하기
"""

import os
from os.path import exists, isdir, isfile

files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR: %s' %file)

for file in files:
    if isfile(file):
        print('FILE: %s' %file)




