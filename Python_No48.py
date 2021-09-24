"""
파일 열고 닫기 (open, close)
"""

f1 = open('text.txt','r')
f2 = open('d/myimages/mypicture1.jpg','rb')

"""
오픈한 파일을 처리하는 코드를 작성
"""

f1.close()
f2.close()


# 파일은 텍스트 파일과 바이너리 파일 두 가지 종류가 있음
# r 또는 rt 텍스트 모드로 읽기
# w 또는 wt 텍스트 모드로 쓰기
# a 또는 at 텍스트 모드로 파일 마지막에 추가하기

# rb 바이너리 모드로 읽기
# wb 바이너리 모드로 쓰기
# ab 바이너리 모드로 파일 마지막에 추가하기