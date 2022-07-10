"""
인터넷에 있는 대용량 파일을 내 pc로 저장하기
"""

from urllib.request import urlopen              

BUFSIZE = 256*1024                         #버프 사이즈를 256kb로 설정

fileurl = 'http://www.python.org/ffp/python/3.8.2/python-3.8.2.exe'   #다운 받을 수 있는 urldmf wlwjd
filename = fileurl.split('/')[-1]       #url에서 파일 이름만 추출하여 filename으로 설정

try:
    with urlopen(fileurl) as f:         #fileurl 을 오픈
        with open(filename,'wb') as h:  #filename을 바이너리 쓰기로 오픈
            buf = f.read(BUFSIZE)       #BUFSIZE만큼 읽어 buf로 지정
            while buf:                  #filename에 buf만큼 저장하고 fileurl에서 buf만큼 읽고 buf로 두는 것을 반복
                h.write(buf)
                buf = f.read(BUFSIZE)
                
except Exception as e:
    print(e)