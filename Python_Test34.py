"""
Check wether there is number that I look for or not
"""
name = [11,22,33]
search = int(input('찾고자 하는 번호: '))

if search in name:
    print(search)
else:
    print("없음")