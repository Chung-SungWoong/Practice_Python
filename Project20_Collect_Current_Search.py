from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# 맥 셀레니움 꺼짐 이슈 있음

driver = webdriver.Chrome(ChromeDriverManager().install())

URL = 'https://signal.bz/news'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

driver.find_element(By.CSS_SELECTOR,'#olLiveIssueKeyword > li:nth-child(1) > a > span.txt_rank').click()

nate_result = driver.find_element(By.CSS_SELECTOR,'#search-option > form:nth-child(1) > fieldset > div.issue-kwd > span > a')

naver_results = driver.find_elements_by_css_selector("abody > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf.emcav > div.RNNXgb > div > div.a4bIc > input")

naver_list = []
for naver_result in naver_results:
    print(naver_result.txt)
    naver_list.append(naver_result.text)


