from ..base import BaseModel
from vk.types.attachments import Photo

class MarketAlbum(BaseModel):
    id: int = None
    owner_id: int = None
    title: str = None
    photo: Photo = None
    count: int = None
    updated_time: int = None