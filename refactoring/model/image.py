from pydantic import BaseModel


class Image(BaseModel):
    shop_id: int
    post_id: str
    image_display_url: str
    image_download_url: str

