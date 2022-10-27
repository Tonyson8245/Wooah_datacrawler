import re

from bs4 import BeautifulSoup
from tqdm import tqdm

from refactoring.config import logger
from refactoring.config.const import PostIdSite


def collect_from_picuki(driver, shop_instagram_id) -> list:
    logger.info('인스타그램 포스트 id 크롤링을 시작합니다')

    logger.info(f'샵({shop_instagram_id}) 프로필 수집 시작')

    # 크롬 실행
    url = PostIdSite.picuki + shop_instagram_id
    logger.info(f'크롬 창 열기:{url}')
    driver.get(url)
    driver.implicitly_wait(2)

    # 크롤링할 웹사이트 html
    html_profile = driver.page_source

    # soup에 넣어주기
    soup_profile = BeautifulSoup(html_profile, 'html.parser')

    # 각 썸네일 컨테이너 모으기
    logger.info('각 썸네일 컨테이너 모으기')
    thumbnail_dom = "body > div.wrapper > div.content.box-photos-wrapper > ul > li"
    thumb_containers = soup_profile.select(thumbnail_dom)

    logger.info(f'샵({shop_instagram_id}) 프로필 수집 완료')
    logger.info(f'수집한 포스트:{len(thumb_containers)}개')

    # 게시물 id 리스트 만들기
    post_ids = list()

    # 포스트 id 수집하기
    logger.info('포스트 id 수집 시작')
    for thumb_rows in tqdm(thumb_containers, desc='포스트 id 수집'):
        post_url = thumb_rows.select('div > div.photo > a')[0]['href']

        driver.get(post_url)

        # 가져온 html 원문으로 beautiful soup 세팅
        html_post = driver.page_source
        soup_post = BeautifulSoup(html_post, 'html.parser')

        regex = re.compile('{}(.*){}'.format(re.escape('let short_code = "'), re.escape('";')))
        text = regex.findall(str(soup_post))
        post_url = text[0]

        post_ids.append(post_url)

    logger.info(f'포스트 id 수집 완료:{len(post_ids)}개')
    logger.info(post_ids)

    return post_ids