"""
URL에 접속하여 HTML 페이지 화면에 출력하기
"""

from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)