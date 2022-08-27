import json
from datetime import datetime

from ShopData import ShopData,ComplexEncoder
from functions import getShopInfo
from selenium import webdriver

driver = webdriver.Chrome()

import time
start = time.time()  # 시작 시간 저장
from selenium import webdriver
import time
from bs4 import BeautifulSoup

# 크롤링 설정
query = '동작구 네일'
bot_qty = 5

# 웹드라이버 생성 및 실행
driver = webdriver.Chrome()
driver.implicitly_wait(3)
try:
    # 크롬 실행
    driver.get("https://m.map.naver.com/search2/search.naver?query=" + query+"&sm=hty&style=v5")
    driver.execute_script("return scrollTo(0,20000000)")
    time.sleep(2)
    # driver.implictily_wait를 쓰기에는 데이터를 가져오는 순간 종료되서, 5초 기다림



    html = driver.page_source

    # soup에 넣어주기
    soup = BeautifulSoup(html, 'html.parser')

    #각 컨테이너 모음
    containers = soup.select("#ct > div.search_listview._content._ctList > ul > li")


    # 샵 갯수 확인
    shoplist = list()

    for i, container in enumerate(containers):
        shopdata = ShopData()

        # 이름 가져오기
        name = container.select_one("div.item_info > a > div > strong").text
        shopdata.name = name

        # 주소 가져오기
        address = container.select_one("div.item_info > div.item_info_inn > div > a").text.strip("주소보기").strip()
        shopdata.address = address

        # 위도 가져오기
        latitude = container['data-latitude']
        shopdata.latitude = latitude

        # 경도 가져오기
        longitude = container['data-longitude']
        shopdata.longitude = longitude

        # 가격 정보 링크 가져오기
        try:
            # 가격 페이지가 없으면 아래 코드에서 오류 발생
            price = container.select_one("div.item_info > div.item_common._itemCommon > a.sp_map.btn_price._linkMenu")
            price_link = "https://m.place.naver.com/nailshop/"+container['data-sid']+"/price"
        except:
            price_link = '없음'
        shopdata.price_link = price_link

        # 예약 링크 가져오기
        try:
            # 가격 페이지가 없으면 아래 코드에서 오류 발생
            reserve = container.select_one("div.item_btn > a.btn_booking._linkBooking")
            reserve_link = "https://m.place.naver.com/nailshop/"+container['data-sid']+"/booking"
        except:
            reserve_link = '없음'
        shopdata.reserve_link = reserve_link

        # 샵 정보 링크 가져오기
        try:
            naver_link = "https://m.place.naver.com/nailshop/"+container['data-sid']
        except:
            naver_link = '없음'
        shopdata.contactInfo.naver_link = naver_link

        # 사진 링크 가져오기
        try:
            photo_link = "https://m.place.naver.com/nailshop/" + container['data-sid'] + '/photo'
        except:
            photo_link = '없음'
        shopdata.photo_link = photo_link

        try:
            getShopInfo(shopdata, driver)
            shoplist.append(shopdata)
        except Exception as e:
            print(e)

        now = datetime.now()
        shopdata.time = now.strftime("%Y/%m/%d, %H:%M:%S")
        print(json.dumps(shopdata.reprJSON(), cls=ComplexEncoder, indent=2, ensure_ascii=False))

finally:
    print(len(shoplist))
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    driver.quit()
