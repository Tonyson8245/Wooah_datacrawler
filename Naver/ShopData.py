import json

class PhoneNumber:
    def __init__(self):
        self.home = ''
        self.private = ''
        self.naver = ''

    def reprJSON(self):
        return dict(home=self.home,private=self.private,naver=self.naver)

class ContactInfo:
    def __init__(self):
        self.phoneNumber = PhoneNumber()
        self.naver_link = ''
        self.instagram = ''
        self.rawData = ''
    def reprJSON(self):
        return dict(phoneNumber=self.phoneNumber,naver_link=self.naver_link, instagram=self.instagram,rawData=self.rawData)

class Business_hour:
    def __init__(self):
        self.raw_data = ''
        # self.holiday = ''
        # self.day_off_week = ''
        # self.day_off_day = ''
        self.mon_work_time = ''
        self.tue_work_time = ''
        self.wes_work_time = ''
        self.thu_work_time = ''
        self.fri_work_time = ''
        self.sat_work_time = ''
        self.sun_work_time = ''
    def reprJSON(self):
        return dict(rawdata = self.raw_data,mon_work_time=self.mon_work_time,tue_work_time=self.tue_work_time,wes_work_time=self.wes_work_time,thu_work_time=self.thu_work_time,fri_work_time=self.fri_work_time,sat_work_time=self.sat_work_time,sun_work_time=self.sun_work_time,)

    def setSameTime(self, time):
        self.mon_work_time = time
        self.tue_work_time = time
        self.wes_work_time = time
        self.thu_work_time = time
        self.fri_work_time = time
        self.sat_work_time = time
        self.sun_work_time = time

class Shopinfo:
    def __init__(self):
        self.introduction = ''
        self.parking = '불가능'
    def reprJSON(self):
        return dict(introduction=self.introduction,parking=self.parking)

class ShopData:
    def __init__(self):
        self.name = ''
        self.address = ''
        self.longitude = ''
        self.latitude = ''
        self.price_link = ''
        self.reserve_link = ''
        self.photo_link = ''
        self.business_hour = Business_hour()
        self.contactInfo = ContactInfo()
        self.shopinfo = Shopinfo()
        self.time = ''
    def reprJSON(self):
        return dict(name=self.name,address=self.address,longitude=self.longitude,latitude=self.latitude,price_link=self.price_link,reserve_link=self.reserve_link,photo_link=self.photo_link,business_hour=self.business_hour,contactInfo=self.contactInfo,shopinfo=self.shopinfo,time=self.time)

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

# doc=ShopData()
# print(json.dumps(doc.reprJSON(), cls=ComplexEncoder, indent=2))



# 기존코드
# import json
#
#
# class PhoneNumber:
#     home = ''
#     private = ''
#     naver = ''
#
# class ContactInfo:
#     phoneNumber = PhoneNumber
#     naver_link = ''
#     kakao_open_chat = ''
#     kakao_channel = ''
#     instagram = ''
#     kakao_id = ''
#
# class Business_hour:
#     holiday = ''
#     day_off_week = ''
#     day_off_day = ''
#     mon_work_time = ''
#     tue_work_time = ''
#     wes_work_time = ''
#     thu_work_time = ''
#     fri_work_time = ''
#     sat_work_time = ''
#     sun_work_time = ''
#
# class Shopinfo:
#     introduction = ''
#     reserve_link = ''
#     parking = ''
#     photo_link = ''
#
# class ShopData:
#     status =  ''
#     name = ''
#     address = ''
#     longitude = ''
#     latitude = ''
#     price_link = ''
#     business_hour = Business_hour
#     contactInfo = ContactInfo
#     shopinfo = Shopinfo
#     time = ''
#     def __init__(self):
#         self.status = 'none'
#
#
#
#
