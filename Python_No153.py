"""
디렉터리를 삭제하기 (os.rmdir)
"""
import os

target_folder = 'temp'
k = input('[%s] 디렉터리를 삭제하시겠습니까? (y/n)' %target_folder)
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제하였습니다.' %target_folder)
    except Exception as e:
        print(e)
