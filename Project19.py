"""
주피터 노트북 코드를 py 코드로 바꿀 필요 있음
"""

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import time

def Selenium_Test():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    URL = 'http://www.google.co.kr/imghp'
    driver.get(url=URL)

    driver.implicitly_wait(time_to_wait=10)

    elem = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input')
    elem.send_keys("바다")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element_by_tag_name("body")
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)

    try:
        driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input').click()

        for i in range(60):
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.1)
        links = []
        images = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input').click()

        for image in images:
            if image.get_attribute('src') is not None:
                links.append(image.get_attribute('src'))
        print('찾은 이미지 개수:', len(links))

        for k, i in enumerate(links):
            url = i
            rllib.request.urlretrieve(url,"/Users/chung_sungwoong/Desktop/Practice/Practice_Python/" +str(k) +".jpg")
        print("다운로드를 완료하였습니다") 
    except:
        pass

    while(True):
        pass

    

Selenium_Test()