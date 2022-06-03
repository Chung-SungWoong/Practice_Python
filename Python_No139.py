"""
텍스트 파일을 한줄씩 읽고 출력하기 (readlines)
"""
f= open('stockcode.txt','r')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' %(line_num+1,line),end='')
f.close()
