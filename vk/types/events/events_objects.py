from ..base import BaseModel

from ..wall_comment import WallComment
from ..attachments.topic import TopicComment

from ..additional import JoinType, BlockReason, AdminLevel
from ..attachments import Photo

import typing

from enum import Enum


class EventMessageAllow(BaseModel):
    user_id: int = None
    key: typing.Optional[str] = None


class EventPhotoCommentNew(BaseModel, WallComment):
    photo_id: int = None
    photo_owner_id: int = None


class EventPhotoCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    photo_id: int = None


class EventVideoCommentNew(BaseModel, WallComment):
    video_id: int = None
    video_owner_id: int = None


class EventVideoCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    video_id: int = None


class EventWallReplyNew(BaseModel, WallComment):
    post_id: int = None
    post_owner_id: int = None


class EventWallReplyDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    post_id: int = None


class EventBoardPostNew(BaseModel, TopicComment):
    topic_id: int = None
    topic_owner_id: int = None


class EventBoardPostDelete(BaseModel):
    topic_id: int = None
    id: int = None


class EventMarketCommentNew(BaseModel, WallComment):
    market_owner_id: int = None
    item_id: int = None


class EventMarketCommentDelete(BaseModel):
    owner_id: int = None
    id: int = None
    user_id: int = None
    item_id: int = None


class EventGroupLeave(BaseModel):
    user_id: int = None
    self: int = None


class EventGroupJoin(BaseModel):
    user_id: int = None
    join_type: JoinType = None


class EventUserBlock(BaseModel):
    admin_id: int = None
    user_id: int = None
    unblock_data: int = None
    reason: BlockReason = None
    comment: str = None


class EventUserUnblock(BaseModel):
    admin_id: int = None
    user_id: int = None
    by_end_date: int = None


class EventPollVoteNew(BaseModel):
    owner_id: int = None
    poll_id: int = None
    option_id: int = None
    user_id: int = None


class EventGroupOfficersEdit(BaseModel):
    admin_id: int = None
    user_id: int = None
    level_old: AdminLevel = None
    level_new: AdminLevel = None


class EventGroupChangeSettingsChangesSectionEnable(Enum):
    status_default = "status_default"
    audio = "audio"
    photo = "photo"
    video = "video"
    market = "market"


class EventGroupChangeSettingsChangesSectionName(Enum):
    title = "title"
    description = "description"
    community_type = "access"
    screen_name = "screen_name"
    public_category = "public_category"
    public_subcategory = "public_subcategory"
    age_limits = "age_limits"
    website = "website"
    enable_section = EventGroupChangeSettingsChangesSectionEnable


class EventGroupChangeSettingsChanges(BaseModel):
    section_name: EventGroupChangeSettingsChangesSectionName = None
    old_value: typing.Any = None
    new_value: typing.Any = None


class EventGroupChangeSettings(BaseModel):
    user_id: int = None
    changes: EventGroupChangeSettingsChanges = None


class EventGroupChangePhoto(BaseModel):
    user_id: int = None
    photo: Photo = None
