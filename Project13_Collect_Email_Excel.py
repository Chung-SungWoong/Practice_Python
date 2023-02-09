

import re
import requests

'''

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

result = re.findall(r'[\w\.-]+@[\w\.-]+',test_string)       # 이메일 형식으로 된 것 확인

results = list(set(results))                                # 중복 제거 코드

print(results)

'''

url = 'https://news.v.daum.net/v/20211129144552297'

headers = {
    'User-Agent':'Mozilla/5.0',
    'Content-Type':'Text/html;charset=utf-8'
}

response = requests.get(url,headers=headers)

results = re.findall(r'[\w\.-]+@[\w\.-]+',response.text)

results = list(set(results))

print(results)