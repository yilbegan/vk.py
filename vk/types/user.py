from ..base import BaseModel

from vk.types.additional import City


class UserCareer(BaseModel):
    group_id: int = None
    company: str = None
    country_id: int = None
    city_id: int = None
    city_name: str = None
    from_: int = None
    until: int = None
    position: str = None

class UserCounters(BaseModel):
    albums: int = None
    videos: int = None
    audios: int = None
    photo: int = None
    notes: int = None
    friends: int = None
    groups: int = None
    online_friends: int = None
    mutual_friends: int = None
    user_videos: int = None
    followers: int = None
    pages: int = None

class UserContacts(BaseModel):
    mobile_phone: str = None
    home_phone: str = None

class User(BaseModel):
    id: int = None
    first_name: str = None
    last_name: str = None
    deactivated: str = None
    is_closed: bool = None
    can_access_closed: bool = None
    about: str = None
    activities: str = None
    bdate: str = None
    blacklisted: int = None
    blacklisted_by_me: int = None
    books: str = None
    can_post: int = None
    can_see_all_posts: int = None
    can_see_audio: int = None
    can_send_friend_request: int = None
    can_write_private_message: int = None
    career: UserCareer = None
    city: City = None
    common_count: int = None
    contacts: UserContacts = None
    counters: UserCounters = None
    country:

