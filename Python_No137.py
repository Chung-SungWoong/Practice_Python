"""
텍스트 파일을 읽고 출력하기 (read)
"""
f = open('stockcode.txt','r')
data = f.read()
print(data)
f.close()