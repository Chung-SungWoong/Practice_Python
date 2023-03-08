"""
세일 정보가 뜨면 알람을 알려주는 프로그램
"""
import telegram
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

while True:
    try:
        driver.get(url='https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu')
        titles = driver.find_elements_by_css_selector("#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr> td:nth-child(2) > div > a > font")
        urls = driver.find_elements_by_css_selector("#revolution_main_table > tbody > tr > td:nth-child(3) > table > tbody > tr> td:nth-child(2) > div > a")
        for i in range(len(titles)):
            if "김치" in titles[i].text:
            message = titles[i].text + "\n" + urls[i].get_attribute('herf')
            print(message)
            token = ''
            bot = telegram.Bot(token)
            bot.sendMessage(chat_id=id,text=message) 


        driver.get(url='https://www.ppomppu.co.kr/zboard.php?id=ppompu')