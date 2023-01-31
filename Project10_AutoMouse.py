"""
네이버에서 자동으로 서울 날씨 검색하는 코드
"""

import pyautogui
import time
import pyperclip

addr_x, addr_y = 966, 264
addr_x2, addr_y2 = 806,163
addr_x3, addr_y3 = 1049, 163
start_x, start_y = 1490, 550
end_x, end_y = 2850, 1350

first = True
region = ["서울 날씨", "시흥 날씨", "의정부 날씨", "부산 날씨"]

pyautogui.moveTo(966,264,0.2)

for region_weather in region:
    # 왜 pyperclip이 안먹히지? --> mac이라 ctrl이 아니라 command 사용해야함
    if first == True:
        pyautogui.moveTo(addr_x,addr_y)
        pyautogui.click()
        first = False
    else:
        pyautogui.mouseDown(addr_x2,addr_y2)
        pyautogui.mouseUp(addr_x3,addr_y3)
    time.sleep(0.2)
    pyperclip.copy(region_weather)
    pyautogui.hotkey("command","v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    save_path = '/Users/chung_sungwoong/Desktop/Practice/Practice_Python//' + region_weather +'.png'
    pyautogui.screenshot(save_path, region=(start_x,start_y, end_x-start_x, end_y-start_y))

"""
for i in range(10):
    print(pyautogui.position())
    time.sleep(1)
"""
