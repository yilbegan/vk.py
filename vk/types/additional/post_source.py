from vk.types.base import BaseModel

class PostSource(BaseModel):
    type: str
    platform: str
    data: str
    url: str