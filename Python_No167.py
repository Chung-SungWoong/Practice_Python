"""
텍스트 파일에 있는 단어 개수 계산하기
"""

with open('mydata.txt','r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수: [%d]' %len(tmp))