"""
현재 디렉터리 확인하고 바꾸기
"""

import os

pdir = os.getcwd(); print(pdir)
os.chdir('..'); print(os.getcwd())
os.chdir(pdir);print(os.getcwd())
