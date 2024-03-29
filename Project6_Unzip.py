import itertools
import zipfile

def unzip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len + 1):
        to_attempt = itertools.product(passwd_string, repeat = len)
        for attempt in to_attemp:
            passwd = ' '.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd = passwd.encode())
                print(f"비밀번호는 {passwd} 입니다")
                break
            except:
                pass

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTWVWXYZ"

zFile = zipfile.ZipFile(r'')
min_len = 1
max_len = 5

unzip_result = unzip(passwd_string,min_len, max_len, zFile)

if unzip_result == 1:
    print('암호찾기 성공')
else:
    print("암호찾기 실패")