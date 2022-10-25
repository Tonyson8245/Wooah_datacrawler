import time
import re

from bs4 import BeautifulSoup

# 크롤링 설정
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def postIdCollector(sub_driver,driver, link):
    driver.implicitly_wait(3)

    # 크롬 실행
    driver.get(shopUrl)
    # driver.execute_script("return scrollTo(0,20000000)")
    time.sleep(2)

    html = driver.page_source

    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')

    thumbContainers = soup.select(
        "body > div.wrapper > div.content.box-photos-wrapper > ul > li")

    # 고정게시물 무시 테스트 코드
    count = 0
    notcrawled = 0

    imageList = list()

    for thumbRows in thumbContainers:
        thumbnails = thumbRows.select('div > div.photo > a')
        for thumbnail in thumbnails:
            link = thumbnail['href']
            # 고정게시물인지 파악
            sub_driver.get(link)

            sub_html = sub_driver.page_source
            sub_soup = BeautifulSoup(sub_html, 'html.parser')

            regex = re.compile('{}(.*){}'.format(re.escape('let short_code = "'), re.escape('";')))
            text = regex.findall(str(sub_soup))
            link = text[0]
            print(link)

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
shopUrl = 'https://www.picuki.com/profile/ouioui.nail'
# 웹 드라이버 생성 및 실행
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

sub_driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

try:
    postIds = postIdCollector(sub_driver,driver, shopUrl)
    print(postIds)
finally:
    driver.quit()
    sub_driver.quit()
