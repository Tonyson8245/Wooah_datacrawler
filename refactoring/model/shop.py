from pydantic import BaseModel


class PhoneNumber(BaseModel):
    home: str
    private: str
    naver: str


class ContactInfo(BaseModel):
    phone_numbers: PhoneNumber
    naver_link: str
    instagram: str
    raw_data: str


class BusinessHour(BaseModel):
    mon_work_time: str
    tue_work_time: str
    wes_work_time: str
    thu_work_time: str
    fri_work_time: str
    sat_work_time: str
    sun_work_time: str
    raw_data: str


class ShopInfo(BaseModel):
    introduction: str
    parking: str = '불가능'


class ShopData(BaseModel):
    name: str
    address: str
    longitude: str
    latitude: str
    price_link: str
    reserve_link: str
    photo_link: str
    business_hour: BusinessHour
    contact_info: ContactInfo
    shop_info: ShopInfo
    time: str


class ShopInstagramIdInfo(BaseModel):
    id: int
    name: str
    instagram_id: str
