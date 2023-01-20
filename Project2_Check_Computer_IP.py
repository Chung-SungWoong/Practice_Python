"""

"""

# 컴퓨터 내부 IP를 찾는 코드
"""
import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print(in_addr.getsockname()[0])
"""
# 컴퓨터 외부 IP를 찾는 코드
"""
import requests
import re

req = requests.get("http://ipconfig.kr/")
out_addr = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)
if out_addr:
    print(out_addr[1])
else:
    print("No match found")
"""
# 내부, 외부 IP 한 번에 출력하는 코드 만들고 실행
import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr",443))
print("내부 IP: ",in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", out_addr)
