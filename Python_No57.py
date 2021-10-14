"""
예외처리 이해하기 3
try~except~finally
"""

try:
    print('안녕하세요.')
    print(param)
except:
    print('예외가 발생했습니다!')
finally:
    print('무조건 실행하는 코드')

# Finally는 예외가 발생하든 발생하지 않든 무조건 실행되는 부분.