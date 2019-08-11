from ..base import BaseModel

class Like(BaseModel):
    user_likes: int = None
    count: int = None