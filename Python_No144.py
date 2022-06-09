"""
파일을 열고 자동으로 닫기
"""

with open('stockcode.txt','r') as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1,line),end='')

