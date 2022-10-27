import requests
from requests import Response

from refactoring.config import logger
from refactoring.config.const import api_base_url


def get_instagram_ids():
    url = api_base_url + '/shops/instagram_ids'

    logger.info('api 요청:'+url)
    response: Response = requests.get(url)

    logger.info('api 요청 결과:' + response.text)

    status_code = response.status_code
    response_result = response.json()

    if status_code is not 200:
        return False, response_result['detail']

    return True, response_result['result']
