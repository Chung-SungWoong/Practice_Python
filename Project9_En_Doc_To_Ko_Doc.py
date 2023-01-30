"""
영어 문서를 한글로 자동번역
"""

import googletrans
from os import linesep

translator = googletrans.Translator()

read_file_path = r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/English_File.txt"
write_file_path = r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Korean_File.txt"

with open(read_file_path,'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path,'a',encoding='UTF8') as f:
        f.write(result1.text + '\n')

"""
str1 = '행복하세요'
result1 = translator.translate(str1,dest='en',src='auto')
print(f"행복하세요 => {result1.text}")

str2 = 'I am happy'
result2 = translator.translate(str2,dest='ko',src='en')
print(f"I am happy => {result2.text}")
"""
