from enum import Enum
from os import path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from refactoring import config
from refactoring.config import logger


class DriverOS(Enum):
    WINDOWS = 'windows'
    LINUX = 'linux'


def get(driver_os: DriverOS):
    # 크롬 드라이버 경로 세팅
    driver_path = path.join(config.base_url, 'chrome_driver', f'chromedriver_{driver_os.value}')

    if driver_os is DriverOS.WINDOWS:
        driver_path += '.exe'

    # 드라이버 옵션 세팅
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    logger.info(f'크롬 드라이버 경로:{driver_path}')
    logger.info(f'크롬 드라이버 옵션:{chrome_options.__dict__.__str__()}')

    return webdriver.Chrome(
        executable_path=driver_path,
        options=chrome_options
    )
