import json
import time
import asyncio

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By


def igdownloader(driver, postId):
    # 링크이동
    driver.get('https://igdownloader.com/')

    url_box = driver.find_element(By.CSS_SELECTOR, "#photo > div > form > div > input")
    act = ActionChains(driver)  # 동작 명령어 지정
    act.send_keys_to_element(url_box, 'https://www.instagram.com/p/' + postId).send_keys(
        Keys.RETURN).perform()  # 아이디 입력, 비밀 번호 입력, 로그인 버튼 클릭 수행
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 결과 컨테이너
    resultContainers = soup.select('main > div > div.section-results > div > div > div > div')

    # 결과 컨테이너 분해
    for container in resultContainers:
        # 제목은 빼고 밑의 사진인 포스트 wrapper 만 사용
        if 'post-wrapper' in container['class'] and 'fa-camera' in container.select_one('div > div.post-type > span')['class']:
            img_showLink = container.select_one('div.post >img')['src']
            img_downLink = container.select_one('a')['href']

            print('SHOW: ' + img_showLink)
            print('DOWNLOAD: ' + img_downLink)


postId = 'Chqy6Iwvs05/'
driver = webdriver.Chrome()
try:
    igdownloader(driver, postId)
finally:
    driver.quit()

# # html 불러오기
# html = driver.page_source
# # soup에 넣어주기
# soup = BeautifulSoup(html, 'html.parser')


# print(json.dumps(imageData.dict(), indent=2, ensure_ascii=False))
