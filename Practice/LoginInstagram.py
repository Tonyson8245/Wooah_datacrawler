import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time




def login(driver):
    driver.set_window_size(414, 800)
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)  # 2

    id_box = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(1) > div > label > input")
    password_box = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(2) > div > label > input")  # 비밀번호 입력창
    login_button = driver.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3) > button')  # 로그인 버튼

    act = ActionChains(driver)  # 동작 명령어 지정
    act.send_keys_to_element(id_box, 'cchd.wooah@gmail.com').send_keys_to_element(password_box, 'dnflemfdml-dkfmaekdna').click(
        login_button).perform()  # 아이디 입력, 비밀 번호 입력, 로그인 버튼 클릭 수행
    time.sleep(10)

    # loginInput = driver.find_element(By.CSS_SELECTOR, 'div > div:nth-child(1) > div > label > input')
    # passInput = driver.find_element(By.CSS_SELECTOR, 'div > div:nth-child(2) > div > label > input')
    # loginBtn = driver.find_element(By.CSS_SELECTOR, 'div > div:nth-child(3) > button > div')
    #
    # loginInput['value'] = 'cchd.wooah@gmail.com'
    # passInput['value'] = 'dnflemfdml-dkfmaekdna'
    # loginBtn.click()
    #
    # time.sleep(5)

    return driver