"""
인터넷을 있는 이미지를 내 pc로 저장하게
"""

from urllib.request import urlopen

imgurl = 'http://www.iaidol.com/img_sample.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname,'wb') as h:
            img = f.read()
            h.write(img)

except Exception as e:
    print(e)