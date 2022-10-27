import time

from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from tqdm import tqdm

from refactoring.config import logger
from refactoring.config.const import instagram_image_download_site, instagram_post_base_url


def collect_post_url(driver, post_id):
    logger.info('인스타그램 포스트 이미지 url 크롤링을 시작합니다')

    # 링크 이동
    logger.info(f'크롬 창 열기:{instagram_image_download_site}')
    driver.get(instagram_image_download_site)

    # 포스트 검색창
    url_input = driver.find_element(By.CSS_SELECTOR, "#photo > div > form > div > input")

    # 원하는 인스타그램 포스트 주소 입력
    act = ActionChains(driver)  # 동작 명령어 지정
    act.send_keys_to_element(url_input, instagram_post_base_url + post_id).send_keys(Keys.RETURN).perform()

    logger.info('포스트 검색')
    time.sleep(5)

    # 크롤링할 웹사이트 html
    html = driver.page_source

    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')

    # 결과 컨테이너
    result_containers = soup.select('main > div > div.section-results > div > div > div > div')

    # 포스트 이미지 url 수집
    display_url = ''
    download_url = ''
    logger.info('포스트 이미지 url 수집 시작')

    for container in tqdm(result_containers, desc='포스트 이미지 url 수집'):
        # 제목은 빼고 밑의 사진인 포스트 wrapper 만 사용
        if 'post-wrapper' in container['class'] and 'fa-camera' in \
                container.select_one('div > div.post-type > span')['class']:
            display_url = container.select_one('div.post >img')['src']
            download_url = container.select_one('a')['href']

    logger.info('포스트 이미지 url 수집 완료')
    logger.info(f'조회용 url:{display_url}')
    logger.info(f'다운로드용 url:{download_url}')

    return display_url, download_url
