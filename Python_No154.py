"""
하위 디렉터리 및  파일 전체 삭제하기 (shutil.rmtree)
"""

import os
import shutil

target_folder = 'd:/devlab/py200/tmp'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' %target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하시겠습니까? (y/n)' %target_folder)
if k == 'y':
    try:
        shutil.rmtree(target_folder)
        print('[%s]의 모든 하위 디렉터리와 파일들을 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)
