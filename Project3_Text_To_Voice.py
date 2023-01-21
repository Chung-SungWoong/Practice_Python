"""
text를 음성으로 tts 읽어주는 코드
"""

from gtts import gTTS
from playsound import playsound

text = "안녕하세요. 이런 기능이 있는지 몰랐어요.신기하네요"

tts = gTTS(text = text, lang = 'ko')
tts.save(r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/hi.mp3")

playsound(r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/hi.mp3")

"""
파일에서 문자를 읽어서 음성으로 출력하는 코드
"""

file_path = r'/Users/chung_sungwoong/Desktop/xxxx.txt'
with open(file_path, 'rt', encoding='utf-16') as f:
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')
tts.save(r"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/texttovoice.mp3")