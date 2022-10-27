import time
from typing import List

from tqdm.auto import tqdm

from refactoring import chrome_driver
from refactoring.api import shop as shop_api, candidate_image as candidate_image_api
from refactoring.config import logger
from refactoring.crawler import *
from refactoring.model.image import Image
from refactoring.model.shop import ShopInstagramIdInfo


def main():
    logger.info('이미지 크롤링 시작')

    # 샵 인스타그램 id 리스트 받아오기
    logger.info('샵 인스타그램 id 리스트 받아오기')
    success, result = shop_api.get_instagram_ids()

    # 샵 인스타그램 리스트 받아오는 것 실패 시 종료
    if not success:
        logger.warn(f'샵 인스타그램 id 리스트 요청 실패:{result}')
        exit()

    # 크롬 드라이버 실행
    driver = chrome_driver.get(chrome_driver.DriverOS.WINDOWS)

    # 크롤링할 post id 후보 딕셔너리 (post_id:shop_id 형식)
    candidate_post_ids: dict = dict()

    # 크롤링할 post id 수집
    logger.info('샵 별 post id 수집 시작')
    for shop_dict in tqdm(result, desc='샵 별 post id 수집'):
        # 샵 별 post id 수집
        shop = ShopInstagramIdInfo(**shop_dict)
        shop_post_ids = post_id_crawler.collect_from_picuki(
            driver=driver,
            shop_instagram_id=shop.instagram_id
        )

        if len(shop_post_ids) == 0:  # 샵 post_ids 빈 값이면 로그 남기기
            logger.warn(f'샵 {shop.name}({shop.id})의 post id 크롤링 결과 없음')
        else:  # 샵 post id 크롤링 성공 시 크롤링 post id 리스트에 추가
            candidate_post_ids[shop_post_ids.__str__()] = shop.id

    logger.info(f'샵 별 post id 수집 완료:{len(candidate_post_ids)}개')
    logger.info(candidate_post_ids)

    # post id 리스트 중 중복된 것 없는지 확인
    logger.info('post id 리스트 중 중복된 것 없는지 확인')
    success, result = candidate_image_api.check_duplication_post_id(post_ids=list(candidate_post_ids.keys()))

    # post id 리스트 중 중복 확인 실패 시 종료
    if not success:
        logger.warn(f'post id 리스트 중 중복 확인 요청 실패:{result}')
        driver.quit()
        exit()

    # 모든 post id가 이미 db에 존재할 경우 종료
    if len(result) == 0:
        logger.warn('크롤링 할 post id 없음')
        driver.quit()
        exit()

    # 실제 크롤링할 post id 리스트 세팅
    crawling_post_ids: list = result
    logger.info(f'크롤링할 post ids:{crawling_post_ids.__str__()}')

    # post id 리스트의 이미지 url 수집
    logger.info('post id 별 이미지 url 수집 시작')
    crawled_images = list()

    for post_id in tqdm(crawling_post_ids, desc='post id 별 이미지 url 수집'):
        # post id 별 이미지 url 수집
        display_url, download_url = image_url_crawler.collect_post_url(
            driver=driver,
            post_id=post_id
        )

        # 이미지 url 세팅
        image = Image(
            shop_id=candidate_post_ids.get(post_id),
            post_id=post_id,
            image_display_url=display_url,
            image_download_url=download_url
        )
        crawled_images.append(image)

    logger.info(f'이미지 크롤링 완료:{len(crawled_images)}')
    logger.info(crawled_images)

    # 수집한 이미지 리스트 db에 저장
    # todo api 만들면 동작 개발해야 함


if __name__ == '__main__':
    main()
