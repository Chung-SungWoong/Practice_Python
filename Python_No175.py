"""
1MB 파일 10개를 합쳐서 10MB 파일로 만들기
"""

BUFSIZE = 256*1024
merge_filename = 'ret.exe'
filelist = ['python-3.5.2.e.x.e_' +str(x) for x in range(10)]

with open(merge_filename,'wb') as f:
    for filename in filelist:
        print('[%s] 합치는 중..' %filename)
        with open(filename,'rb') as h:
            buf = h.read(BUFSIZE)
            while buf:
                f.write(buf)
                buf = h.read(BUFSIZE)


print('파일 합치기가 완료되었습니다.')