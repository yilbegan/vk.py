from enum import Enum, IntEnum
from vk.types import BaseModel

class SimpleResponse(BaseModel):
    response: int = None

class ItemsResponse(BaseModel):
    count: int = None
    items: int = None

