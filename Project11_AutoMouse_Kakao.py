import pyautogui
import pyperclip
import time
import threading
import sys
import schedule

# pyautogui의 좌표값이 다른 오류가 있어 찾아본 결과 맥의 스크린샷 기능과 pyautog이 메세지는 자동으로 보내는 메세지입니다!!
# ui에서 사용하는 스크린 샷 기능의 좌표 설정이 달라 에러가 나는 듯 함
def send_message():
    picPosition = pyautogui.locateCenterOnScreen(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Kakao_My_Pic.png')
    print(picPosition)
    pyautogui.move(picPosition)
    if picPosition is None:
        picPosition = pyautogui.locateOnScreen(r'/Users/chung_sungwoong/Desktop/Practice/Practice_Python/Kakao_My_Pic2.png')
        print(picPosition)
        if picPosition is None:
            print("사진이 화면에 없습니다.")
            sys.exit()

    pyautogui.moveTo(picPosition)
    pyautogui.doubleClick()

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지입니다!!")
    pyautogui.hotkey("command",'v')
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)