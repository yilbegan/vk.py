from ..base import BaseModel
from . import events_list as events
from . import events_objects as EventsObjects

from ..message import Message
from ..attachments import Photo
from ..attachments import Audio
from ..attachments import Video

from ..wall_post import WallPost

from enum import Enum

import typing


# https://vk.com/dev/groups_events


class BaseEvent(BaseModel):
    group_id: int = None


class EventMessageNew(BaseEvent):
    type: events.Message.MESSAGE_NEW = None
    object: Message = None


class EventMessageReply(EventMessageNew):
    type: events.Message.MESSAGE_REPLY = None


class EventMessageAllow(BaseEvent):
    type: events.Message.MESSAGE_ALLOW = None
    object: EventsObjects.EventMessageAllow = None


class EventMessageDeny(BaseEvent):
    type: events.Message.MESSAGES_DENY = None
    object: EventsObjects.EventMessageAllow = None


class EventPhotoNew(BaseEvent):
    type: events.Photo.PHOTO_NEW = None
    object: Photo = None


class EventPhotoCommentNew(BaseEvent):
    type: events.Photo.PHOTO_COMMENT_NEW = None
    object: EventsObjects.EventPhotoCommentNew = None


class EventPhotoCommentEdit(EventPhotoCommentNew):
    type: events.Photo.PHOTO_COMMENT_EDIT = None


class EventPhotoCommentRestore(EventPhotoCommentNew):
    type: events.Photo.PHOTO_COMMENT_RESTORE = None


class EventPhotoCommentDelete(BaseEvent):
    type: events.Photo.PHOTO_COMMENT_DELETE = None
    object: EventsObjects.EventPhotoCommentDelete = None


class EventAudioNew(BaseEvent):
    type: events.Audio.AUDIO_NEW = None
    object: Audio = None


class EventVideoNew(BaseEvent):
    type: events.Video.VIDEO_NEW = None
    object: Video = None


class EventVideoCommentNew(BaseEvent):
    type: events.Video.VIDEO_COMMENT_NEW = None
    object: EventsObjects.EventVideoCommentNew = None


class EventVideoCommentEdit(EventVideoCommentNew):
    type: events.Video.VIDEO_COMMENT_EDIT = None


class EventVideoCommentRestore(EventVideoCommentNew):
    type: events.Video.VIDEO_COMMENT_RESTORE = None


class EventVideoCommentDelete(BaseEvent):
    type: events.Video.VIDEO_COMMENT_DELETE = None
    object: EventsObjects.EventVideoCommentDelete = None


class EventWallPostNew(BaseEvent):
    type: events.Wall.WALL_POST_NEW = None
    object: WallPost = None


class EventWallRepost(EventWallPostNew):
    type: events.Wall.WALL_REPOST = None


class EventWallReplyNew(BaseEvent):
    type: events.Wall.WALL_REPLY_NEW = None
    object: EventsObjects.EventWallReplyNew = None


class EventWallReplyEdit(EventWallReplyNew):
    type: events.Wall.WALL_REPLY_EDIT = None


class EventWallReplyRestore(EventWallReplyNew):
    type: events.Wall.WALL_REPLY_RESTORE = None


class EventWallReplyDelete(BaseEvent):
    type: events.Wall.WALL_REPLY_DELETE = None
    object: EventsObjects.EventWallReplyDelete = None


class EventBoardPostNew(BaseEvent):
    type: events.Board.BOARD_POST_NEW = None
    object: EventsObjects.EventBoardPostNew = None


class EventBoardPostEdit(EventBoardPostNew):
    type: events.Board.BOARD_POST_EDIT = None


class EventBoardPostRestore(EventBoardPostNew):
    type: events.Board.BOARD_POST_RESTORE = None


class EventBoardPostDelete(BaseEvent):
    type: events.Board.BOARD_POST_DELETE = None
    object: EventsObjects.EventBoardPostDelete = None


class EventMarketCommentNew(BaseEvent):
    type: events.Market.MARKET_COMMENT_NEW = None
    object: EventsObjects.EventMarketCommentNew = None


class EventMarketCommentEdit(EventMarketCommentNew):
    type: events.Market.MARKET_COMMENT_EDIT = None


class EventMarketCommentRestore(EventMarketCommentNew):
    type: events.Market.MARKET_COMMENT_RESTORE = None


class EventMarketCommentDelete(BaseEvent):
    type: events.Market.MARKET_COMMENT_DELETE = None
    object: EventsObjects.EventMarketCommentDelete = None


class EventGroupLeave(BaseEvent):
    type: events.Users.GROUP_LEAVE = None
    object: EventsObjects.EventGroupLeave = None


class EventGroupJoin(BaseEvent):
    type: events.Users.GROUP_JOIN = None
    object: EventsObjects.EventGroupJoin = None


class EventUserBlock(BaseEvent):
    type: events.Users.USER_BLOCK = None
    object: EventsObjects.EventUserBlock = None


class EventUserUnblock(BaseEvent):
    type: events.Users.USER_UNBLOCK = None
    object: EventsObjects.EventUserUnblock = None


class EventPollVoteNew(BaseEvent):
    type: events.Other.POLL_VOTE_NEW = None
    object: EventsObjects.EventPollVoteNew = None


class EventGroupOfficersEdit(BaseEvent):
    type: events.Other.GROUP_OFFICERS_EDIT = None
    object: EventsObjects.EventGroupOfficersEdit = None


class EventGroupChangeSettings(BaseEvent):
    type: events.Other.GROUP_CHANGE_SETTINGS = None
    object: EventsObjects.EventGroupChangeSettings = None


class EventGroupChangePhoto(BaseEvent):
    type: events.Other.GROUP_CHANGE_PHOTO = None
    object: EventsObjects.EventGroupChangePhoto = None
