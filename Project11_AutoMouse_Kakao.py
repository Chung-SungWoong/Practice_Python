"""

"""
import pyautogui
import pyperclip
import time
import threading

picPosition = pyautogui.locateOnScreen(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Kakao_My_Pic.png')
print(picPosition)

if picPosition is None:
    picPosition = pyautogui.locateOnScreen(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Kakao_My_Pic2.png')
    print(picPosition)

clickPosition = pyautogui.center(picPosition)
pyautogui.doubleClick(clickPosition)

pyperclip.copy("이 메세지는 자동으로 보내는 메세지입니다!!")
pyautogui.hotkey("command",'v')
time.sleep(1.0)

pyautogui.write(["enter"])
time.sleep(1.0)

pyautogui.write(["escape"])
time.sleep(1.0)