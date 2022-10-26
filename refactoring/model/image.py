from pydantic import BaseModel


class Image(BaseModel):
    shop_id: int
    origin_post_url: str
    image_display_url: str
    image_download_url: str

