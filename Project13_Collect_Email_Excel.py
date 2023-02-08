"""

"""

import re

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

print(result)
