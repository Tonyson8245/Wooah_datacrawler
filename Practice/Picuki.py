import time
import re

from bs4 import BeautifulSoup
from tqdm import tqdm
# 크롤링 설정
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def postIdCollector(sub_driver,driver, shopId):
    shopUrl = 'https://www.picuki.com/profile/'

    try:
        # 크롬 실행
        driver.get(f'{shopUrl}{shopId}')
        driver.implicitly_wait(2)

        html = driver.page_source

        # soup에 넣어주기
        soup = BeautifulSoup(html, 'html.parser')

        thumbContainers = soup.select(
            "body > div.wrapper > div.content.box-photos-wrapper > ul > li")

        # 고정게시물 무시 테스트 코드
        imageList = list()
        for thumbRows in tqdm(thumbContainers):
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

                imageList.append(link)
    finally:
        driver.quit()
        sub_driver.quit()

    return imageList


# 제공 받아야하는 부분
shopId = str("innail_yd/")

# 웹 드라이버 생성 및 실행
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(ChromeDriverManager().install())

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)
sub_driver = webdriver.Chrome('./chromedriver', chrome_options=chrome_options)

postIds = postIdCollector(sub_driver,driver,shopId)
print(postIds)



