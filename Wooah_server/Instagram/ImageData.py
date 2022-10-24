from pydantic import BaseModel
import json


class ImageData(BaseModel):
    shopName: str
    postId: str
    ImageUrl: str

    def parse_json(self):
        return dict(shopName=self.shopName, postId=self.postId, ImageUrl=self.ImageUrl)

# if __name__ == '__main__':
#     test = A(shopName='하이', postId='123123', ImageUrl='ww.naber.co')

# print(json.dumps(test.dict(),indent=2, ensure_ascii=False) )  # pydantic 패키지의 BaseModel을 상속받으면 dict()함수로 직렬화를 간편하게 할 수 있음
