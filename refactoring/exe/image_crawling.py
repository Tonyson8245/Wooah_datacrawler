'''
1. api 서버에 전체 partner shop id 요청
2. 샵 ids로 샵 별 post id 수집
    -> 잘못된 샵 url인 경우 로그
        if len(post_ids) == 0:
            logger.warn()
3. post ids로 포스트별 image url 수집
    -> 잘못된 post url인 경우 로그
        if display_url is None or download_url is None:
            logger.warn()
4. 수집한 데이터 api에 요청해 저장
5. 실행 결과 로깅
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from refactoring.config import logger


def test():
    # 제공 받아야하는 부분
    shopUrl = 'https://www.instagram.com/ouioui.nail/'
    # 웹 드라이버 생성 및 실행
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('./chromedriver', options=chrome_options)

    try:
        postIds = postIdCollector(driver, shopUrl)
        print(postIds)
    finally:
        driver.quit()


def main():
    logger.debug('hello mate!')
    logger.info('this is the info for you')
    logger.warn('WARNNING!')


if __name__ == '__main__':
    main()
