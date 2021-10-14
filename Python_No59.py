"""
예외처리 이해하기 5
try~except 특정 예외
"""

import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt:
    print('사용자에[ 의해 프로그램이 중단되었습니다')

"""
코드에서 특정 예외 상황이 발생했을 때만 except에서 처리할 수 있는 방법으로 except 다음에 특정 예외를 명시해주는 방법이 있다.
예제 코드는 사용자가 키보드로 ctrl + c를 누를 때 까지 1씩 증가하는 숫자를 0.5초마다 화면에 표시한다.
"""