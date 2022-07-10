"""
10mb 파일을 1mb 파일 10개로 분리하기
"""

filename = 'python-3.8.2.exe'
subsize = 1024*1024*3
suffix = 0

with open(filename,'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename,'wb') as h:
            h.write(buf)
            print('[%s] 완료'%subfilename)

        buf = f.read(subsize)
        suffix += 1
