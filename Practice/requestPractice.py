import requests

query = '동작구 네일'
URL = "https://m.map.naver.com/search2/search.naver?query=" + query+"&sm=hty&style=v5"
shop_URL = "https://m.place.naver.com/nailshop/1632888413/price"
response = requests.get(shop_URL)
print(response.status_code)
print(response.text)

