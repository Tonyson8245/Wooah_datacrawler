import requests

from refactoring.config import const, logger
from refactoring.model.image import Image

api_url = const.api_base_url + '/candidate-images'


def check_duplication_post_id(post_ids: list):
    url = api_url + '/post_ids/check'
    body = {
        'post_ids': post_ids
    }

    logger.info('api 요청:' + url)
    response = requests.post(url=url, data=body)

    logger.info('api 요청 결과:' + response.text)

    status_code = response.status_code
    response_result = response.json()

    if status_code is not 200:
        return False, response_result['detail']

    return True, response_result['result']


def post_multi(images: list[Image]):
    url = api_url
    body = {
        # todo 요청 바디 내용
    }

    logger.info('api 요청:' + url)
    response = requests.post(url=url, data=body)

    logger.info('api 요청 결과:' + response.text)

    # todo 요청 이후 응답값 처리 코드 작성
