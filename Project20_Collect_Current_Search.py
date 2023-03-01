from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 맥 셀레니움 꺼짐 이슈 있음

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://signal.bz/news'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

driver.find_element(By.CSS_SELECTOR,'#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank').click()

# 네이트
nate_results = driver.find_element(By.CSS_SELECTOR,'#search-option > form:nth-child(1) > fieldset > div.issue-kwd > span > a')
nate_list = []
for naver_result in nate_results:
    print(naver_result.txt)
    nate_list.append(naver_result.text)
    
# 네이버
naver_results = driver.find_elements_by_css_selector("abody > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input")
naver_list = []
for naver_result in naver_results:
    print(naver_result.txt)
    naver_list.append(naver_result.text)

# 줌
URL = 'https://zum.com'

driver.find_element(By.CSS_SELECTOR,'#app > div > header > div.search_bar > div > field-set > div > input[type=text]').send_keys("아무거나 검색")
time.sleep(0.5)
driver.find_element(By.CSS_SELECTOR,'#app > div > header > div.search_bar > div > field-set > div > button.search').click()
time.sleep(1)
zoom_results = driver.find_elements_by_css_selector('#issue_wrap > ul > li > div > a:nth-child(1) > span.txt')

zoom_list = []
for zoom_result in zoom_results:
    print(zoom_result.text)
    zoom_list.append(zoom_result.text)

print("네이버", naver_list)
print("네이트",nate_list)
print("줌",zoom_list)

