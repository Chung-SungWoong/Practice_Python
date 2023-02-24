from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# 맥 셀레니움 꺼짐 이슈 있음

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://www.google.co.kr'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

