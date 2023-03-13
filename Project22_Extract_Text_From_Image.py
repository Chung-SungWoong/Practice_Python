"""
이미지 인식을 위한 OCR 프로그램 설치 필요
mac 사용중이라 우선은 OCR 프로그램 설치는 미뤄두고 코드부터
"""

from PIL import Image
import pytesseract

image_path = r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Project22_한글이미지.png'

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(Image.open(image_path),lang='kor')

print(text)

with open(r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Project22_한글텍스트.txt",'w',encoding="utf8") as f:
    f.write(text)

# 사용 가능한 언어 확인
pytesseract.pytesseract.teseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
languages = pytesseract.get_languages(config=' ')
print(languages)

