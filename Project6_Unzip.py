import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTWVWXYZ"

zFile = zipfile.ZipFile(r'')

for len in range(1,4):
    to_attemp = itertools.product(passwd_string, repeat = len)
    for attempt in to_attemp:
        passwd = ' '.join(attempt)
        print(passwd)

