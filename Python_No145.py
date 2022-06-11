"""
파일의 특정 부분만 복사하기
"""

spos = 105
size = 500

f = open('stockcode.txt','r')
h = open('stockcode_park.txt','w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()