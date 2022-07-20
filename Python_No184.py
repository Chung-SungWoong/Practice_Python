"""
웹서버 로그 처리하기1
"""

pageviews = 0

with open('access_log','r') as f:
    logs =f.readlines()
    for log in logs:
        log = log.split()
        status = log[8]
        if status =='200':
            pageviews += 1

print('총 페이지뷰: [%d]' %pageviews)

