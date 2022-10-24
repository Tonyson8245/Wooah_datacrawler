import time

from bs4 import BeautifulSoup

# 크롤링 설정
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def postIdCollector(driver, link):
    driver.implicitly_wait(3)

    # 크롬 실행
    driver.get(shopUrl)
    # driver.execute_script("return scrollTo(0,20000000)")
    time.sleep(2)

    html = driver.page_source

    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')

    # 처음 뜨는 거 쿠키 팝업 닫기 동작
    cookie_wd = driver.find_element(By.CSS_SELECTOR,
                                    'div > div > div > div > div > div > div > div > section > nav > div > div > div > div > div > div > div > button')
    cookie_wd.click()
    time.sleep(2)

    driver.execute_script("return scrollTo(0,20000000)")
    time.sleep(10)

    # 각 썸네일 컨테이너 모음
    thumbContainers = soup.select(
        "div > div > div > div > div > div > div > div > div> section > main > div > div> article > div > div")

    # 고정게시물 무시 테스트 코드
    count = 0
    notcrawled = 0

    imageList = list()

    for thumbRows in thumbContainers:
        thumbnails = thumbRows.select('div > div > a')
        for thumbnail in thumbnails:
            link = thumbnail['href'].lstrip('/p/')
            # 고정게시물인지 파악
            try:
                pin = thumbnail.select_one('div > div > svg')['aria-label']
            except:
                pin = "일반 게시물"

            if pin == "고정 게시물":
                notcrawled += 1
            else:
                imageList.append(link)
                count += 1

    print('수집됨:' + str(count))
    print('무시함:' + str(notcrawled))

    return imageList


# 제공 받아야하는 부분
shopUrl = 'https://www.instagram.com/ouioui.nail/'
# 웹 드라이버 생성 및 실행
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)


try:
    postIds = postIdCollector(driver, shopUrl)
    print(postIds)
finally:
    driver.quit()
