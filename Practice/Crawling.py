from selenium import webdriver

driver = webdriver.Chrome()


from selenium import webdriver
import time
from bs4 import BeautifulSoup

# 크롤링 설정
query = '치킨'
bot_qty = 5

# 웹드라이버 생성 및 실행
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 크롬 실행

driver.get("https://m.map.naver.com/search2/search.naver?query=" + query+"&sm=hty&style=v5")
# time.sleep(5)

driver.execute_script("return scrollTo(0,20000000)")
time.sleep(5)
# driver.implictily_wait를 쓰기에는 데이터를 가져오는 순간 종료되서, 5초 기다림



html = driver.page_source

# soup에 넣어주기
soup = BeautifulSoup(html, 'html.parser')
names = soup.select("#ct > div > ul > li > div.item_info > a > div > strong")

# 샵 갯수 확인
shopQty = len(names)







# # 검색
# search_box = driver.find_element(By.CSS_SELECTOR,'#ct > div.search._searchView > div.Nsearch > form > div > div.Nsearch_box > div > span.Nbox_text > input')
# search_box_open = driver.find_element(By.CSS_SELECTOR,'#header > header > div.Nsearch._searchKeywordView._searchGuide > div > div > div > span.Nbox_tool > button.Nbox_button.Nbox_search._search')
# search_box_click = driver.find_element(By.CSS_SELECTOR,'#ct > div.search._searchView > div.Nsearch > form > div > div.Nsearch_box > div > span.Nbox_tool > button.Nbox_button.Nbox_search._search')
#
# search_box_open.click()
# time.sleep(2)
# search_box.send_keys('마라탕')
# time.sleep(2)
# search_box_click.click()
# time.sleep(2)

# 검색 결과만 가져오는 코드
# raw = driver.find_element(By.CSS_SELECTOR,"#ct > div.search_listview._content._ctList > ul")
# time.sleep(5)

# 페이지 소스 가져오기
