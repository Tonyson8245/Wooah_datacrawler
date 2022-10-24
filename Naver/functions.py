# 샵 정보 가져오는 함수
import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from ShopData import ShopData, ComplexEncoder
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('./chromedriver',chrome_options=chrome_options)


def getShopInfo(shopdata,driver):
    # 웹 드라이버 생성 및 실행
    driver.implicitly_wait(3)

    # 크롬 실행
    driver.get(shopdata.contactInfo.naver_link)
    # driver.execute_script("return scrollTo(0,20000000)")
    time.sleep(1)
    # driver.implictily_wait를 쓰기에는 데이터를 가져오는 순간 종료되서, 5초 기다림

    # 크롤링할 페이지 사전 준비 (드롭 다운 눌러 두기등...)
    html = driver.page_source
    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')
    # 샵 정보 컨테이너
    containerSelector = '#app-root > div > div > div > div > div > div > div > ul'
    InfoContainer = soup.select_one(containerSelector)
    # 정보 리스트 추출
    listSelector = 'li'
    infoList = InfoContainer.select(listSelector)
    # 정보 리스트 열기
    for i, info in enumerate(infoList):
        # 정보 종류 확인

        # 영업시간 있는 info 찾기
        if "영업시간" in info.text or "0507" in info.text or "홈페이지" in info.text or "편의" in info.text or "설명" in info.text:
            # 해당 info 의 클래스 찾기
            classes = info.get('class')
            classes_str = '.'.join(s for s in classes)
            path = "'div > div > div > div > div > div > div > ul > li." + classes_str + " > div > a'"
            # 영업시간 탭 열기 : webdriver쓰려고 했지만 상단의 타이틀 클릭이랑 같이 발생되어 오류 발생되서, 브라우저 콘솔에 자바 스크립트로 명령어 실행 시킨
            try:
                driver.execute_script(
                "return document.querySelector(" + path +").click()")
            except:
                pass
                # print('클릭 실패 :' + info.text)
    # ---------------- 사전 준비 끝 ------------------\

    new_html = driver.page_source
    # soup에 넣어주기
    new_soup = BeautifulSoup(new_html, 'html.parser')
    # 샵 정보 컨테이너
    new_containerSelector = '#app-root > div > div > div > div > div > div > div > ul'
    new_InfoContainer = new_soup.select_one(new_containerSelector)
    # 정보 리스트 추출
    new_listSelector = 'li'
    new_infoList = new_InfoContainer.select(new_listSelector)
    for i, info in enumerate(new_infoList):
        if "영업시간" in info.text:
            # 월로 시작하는 span 값의 시간을 가져온다.
            worktimeList = info.select('div > span')
            for worktime in worktimeList:
                if "매일" in worktime.text:
                    shopdata.business_hour.setSameTime(worktime.text.lstrip('매일'))
                # 월11:00 - 21:00 형태기 떄문에 '월'이라는 문자를 지운다.
                elif "월" in worktime.text:
                    shopdata.business_hour.mon_work_time = worktime.text.lstrip('월')
                elif "화" in worktime.text:
                    shopdata.business_hour.tue_work_time = worktime.text.lstrip('화')
                elif "수" in worktime.text:
                    shopdata.business_hour.wes_work_time = worktime.text.lstrip('수')
                elif "목" in worktime.text:
                    shopdata.business_hour.thu_work_time = worktime.text.lstrip('목')
                elif "금" in worktime.text:
                    shopdata.business_hour.fri_work_time = worktime.text.lstrip('금')
                elif "토" in worktime.text:
                    shopdata.business_hour.sat_work_time = worktime.text.lstrip('토')
                elif "일" in worktime.text:
                    shopdata.business_hour.sun_work_time = worktime.text.lstrip('일')
                else:
                    shopdata.business_hour.raw_data += worktime.text  + '\n'
        elif "설명" in info.text:
            shopdata.shopinfo.introduction = info.select_one('div').text
        elif "편의" in info.text:
            if "주차," in info.select_one('div').text:
                shopdata.shopinfo.parking = "가능"
        elif "홈페이지" in info.text:
            for linkContainer in info.select('div > div'):
                link = linkContainer.select_one('a')['href']
                if "instagram" in link:
                    shopdata.contactInfo.instagram = link
                else:
                    shopdata.contactInfo.rawData += link + '\n'
        # 전화번호가 있는 조건, 제일 앞 4글자에 0507 또는 - 가 포함되어있을시
        elif info.text[0:4]=='0507' or '-' in info.text[0:4]:
            numberContainer = info.select_one('div > span')
            number = numberContainer.text
            if number[0:4] == '0507':
                shopdata.contactInfo.phoneNumber.naver = number
            elif number[0:4] == '010-':
                shopdata.contactInfo.phoneNumber.private = number
            else:
                shopdata.contactInfo.phoneNumber.home = number


# shopdata = ShopData()
# shopdata.contactInfo.naver_link = 'https://m.place.naver.com/nailshop/37589092'
# driver = webdriver.Chrome()
# getShopInfo(shopdata,driver)
# print(json.dumps(shopdata.reprJSON(), cls=ComplexEncoder, indent=2, ensure_ascii=False))



