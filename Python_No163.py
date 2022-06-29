"""
URL에서 호스트 도메인 추출하기
"""
url = 'http://news.naver.com/main/read.nhn?mode=LSD&mid-shm%sid1=105&oid=028&aid=002334601'

tmp = url.split('/')
domain = tmp[2]
print(domain)