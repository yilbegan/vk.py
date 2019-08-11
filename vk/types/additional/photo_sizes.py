from vk.types.base import BaseModel

class PhotoSizes(BaseModel):
    src: str
    width: int
    height: int
    type: str
