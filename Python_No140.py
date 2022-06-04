"""
화면에서 사용자 입력을 받고 파일로 쓰기
"""

text = input('파일에 저장할 내용을 입력하세요: ')
f = open('mydata.text','w')
f.write(text)
f.close()

