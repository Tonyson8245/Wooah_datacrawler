import time

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from refactoring.config import logger
from refactoring.config.const import instagram_image_download_site, instagram_post_base_url


def collect_instagram_post_id(driver, url) -> list:
    logger.info('인스타그램 포스트 id 크롤링을 시작합니다')

    # 크롬 실행
    driver.get(url)
    logger.info('크롬 실행')
    time.sleep(5)

    html = driver.page_source

    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')

    # 처음 나타나는 쿠키 팝업 닫기
    popup_dom = 'div > div > div > div > div > div > div > div > section > nav > div > div > div > div > div > div > div > button'
    cookie_wd = driver.find_element(By.CSS_SELECTOR, popup_dom)
    cookie_wd.click()
    logger.info('처음 나타나는 쿠키 팝업 닫기')
    time.sleep(3)

    # 스트롤 맨 밑으로 이동
    driver.execute_script("return scrollTo(0,20000000)")
    logger.info('스트롤 맨 밑으로 이동')
    time.sleep(10)

    # 각 썸네일 컨테이너 모으기
    thumbnail_dom = "div > div > div > div > div > div > div > div > div> section > main > div > div> article > div > div"
    thumb_containers = soup.select(thumbnail_dom)
    logger.info('각 썸네일 컨테이너 모으기')

    # 게시물 id 리스트 만들기
    post_ids = list()
    logger.info('포스트 id 수집 시작')

    for thumb_rows in thumb_containers:
        logger.info('썸네일 row 별 수집')

        thumbnails = thumb_rows.select('div > div > a')
        logger.info(f'썸네일 개수:{thumbnails}')
        before_count = len(post_ids)
        logger.info(f'포스트 id 수집 전 개수:{len(post_ids)}')

        for thumbnail in thumbnails:
            link = thumbnail['href'].lstrip('/p/')
            pin = thumbnail.select_one('div > div > svg')['aria-label']
            if pin:
                post_ids.append(link)

        after_count = len(post_ids) - before_count
        logger.info(f'포스트 id 수집된 개수:{after_count}')

    logger.info('포스트 id 수집 완료')
    logger.info(post_ids)

    return post_ids


def collect_post_url(driver, post_id):
    logger.info('인스타그램 포스트 이미지 url 크롤링을 시작합니다')

    # 링크 이동
    driver.get(instagram_image_download_site)

    # 포스트 검색창
    url_input = driver.find_element(By.CSS_SELECTOR, "#photo > div > form > div > input")

    # 원하는 인스타그램 포스트 주소 입력
    act = ActionChains(driver)  # 동작 명령어 지정
    act.send_keys_to_element(url_input, instagram_post_base_url + post_id).send_keys(Keys.RETURN).perform()

    logger.info('포스트 검색')
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 결과 컨테이너
    result_containers = soup.select('main > div > div.section-results > div > div > div > div')

    # 포스트 이미지 url 수집
    display_url = ''
    download_url = ''
    logger.info('포스트 이미지 url 수집 시작')

    for container in result_containers:
        # 제목은 빼고 밑의 사진인 포스트 wrapper 만 사용
        if 'post-wrapper' in container['class'] and 'fa-camera' in \
                container.select_one('div > div.post-type > span')['class']:
            display_url = container.select_one('div.post >img')['src']
            download_url = container.select_one('a')['href']

    logger.info('포스트 이미지 url 수집 완료')
    logger.info(f'조회용 url:{display_url}')
    logger.info(f'다운로드용 url:{download_url}')

    return display_url, download_url
