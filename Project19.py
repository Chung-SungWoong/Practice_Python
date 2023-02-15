from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'http://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


elem = driver.find_element(By.CSS_SELECTOR,'body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input')
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)
