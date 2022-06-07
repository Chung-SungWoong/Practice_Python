"""
텍스트 파일 복사하기
"""

f = open('stockcode.txt','r')
h = open('stockcode_copy.txt','w')

data = f.read()
h.write(data)

f.close()
h.close()
