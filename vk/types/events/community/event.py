from vk.types.base import BaseModel
from . import events_list as events
from . import events_objects as EventsObjects

from vk.types.message import Message
from vk.types.attachments import Photo
from vk.types.attachments import Audio
from vk.types.attachments import Video

from vk.types.wall_post import WallPost

# https://vk.com/dev/groups_events


class BaseEvent(BaseModel):
    group_id: int = None


class MessageNew(BaseEvent):
    type: events.Message.MESSAGE_NEW = None
    object: Message = None


class MessageReply(MessageNew):
    type: events.Message.MESSAGE_REPLY = None


class MessageAllow(BaseEvent):
    type: events.Message.MESSAGE_ALLOW = None
    object: EventsObjects.MessageAllow = None


class MessageDeny(BaseEvent):
    type: events.Message.MESSAGES_DENY = None
    object: EventsObjects.MessageAllow = None


class PhotoNew(BaseEvent):
    type: events.Photo.PHOTO_NEW = None
    object: Photo = None


class PhotoCommentNew(BaseEvent):
    type: events.Photo.PHOTO_COMMENT_NEW = None
    object: EventsObjects.PhotoCommentNew = None


class PhotoCommentEdit(PhotoCommentNew):
    type: events.Photo.PHOTO_COMMENT_EDIT = None


class PhotoCommentRestore(PhotoCommentNew):
    type: events.Photo.PHOTO_COMMENT_RESTORE = None


class PhotoCommentDelete(BaseEvent):
    type: events.Photo.PHOTO_COMMENT_DELETE = None
    object: EventsObjects.PhotoCommentDelete = None


class AudioNew(BaseEvent):
    type: events.Audio.AUDIO_NEW = None
    object: Audio = None


class VideoNew(BaseEvent):
    type: events.Video.VIDEO_NEW = None
    object: Video = None


class VideoCommentNew(BaseEvent):
    type: events.Video.VIDEO_COMMENT_NEW = None
    object: EventsObjects.VideoCommentNew = None


class VideoCommentEdit(VideoCommentNew):
    type: events.Video.VIDEO_COMMENT_EDIT = None


class VideoCommentRestore(VideoCommentNew):
    type: events.Video.VIDEO_COMMENT_RESTORE = None


class VideoCommentDelete(BaseEvent):
    type: events.Video.VIDEO_COMMENT_DELETE = None
    object: EventsObjects.VideoCommentDelete = None


class WallPostNew(BaseEvent):
    type: events.Wall.WALL_POST_NEW = None
    object: WallPost = None


class WallRepost(WallPostNew):
    type: events.Wall.WALL_REPOST = None


class WallReplyNew(BaseEvent):
    type: events.Wall.WALL_REPLY_NEW = None
    object: EventsObjects.WallReplyNew = None


class WallReplyEdit(WallReplyNew):
    type: events.Wall.WALL_REPLY_EDIT = None


class WallReplyRestore(WallReplyNew):
    type: events.Wall.WALL_REPLY_RESTORE = None


class WallReplyDelete(BaseEvent):
    type: events.Wall.WALL_REPLY_DELETE = None
    object: EventsObjects.WallReplyDelete = None


class BoardPostNew(BaseEvent):
    type: events.Board.BOARD_POST_NEW = None
    object: EventsObjects.BoardPostNew = None


class BoardPostEdit(BoardPostNew):
    type: events.Board.BOARD_POST_EDIT = None


class BoardPostRestore(BoardPostNew):
    type: events.Board.BOARD_POST_RESTORE = None


class BoardPostDelete(BaseEvent):
    type: events.Board.BOARD_POST_DELETE = None
    object: EventsObjects.BoardPostDelete = None


class MarketCommentNew(BaseEvent):
    type: events.Market.MARKET_COMMENT_NEW = None
    object: EventsObjects.MarketCommentNew = None


class MarketCommentEdit(MarketCommentNew):
    type: events.Market.MARKET_COMMENT_EDIT = None


class MarketCommentRestore(MarketCommentNew):
    type: events.Market.MARKET_COMMENT_RESTORE = None


class MarketCommentDelete(BaseEvent):
    type: events.Market.MARKET_COMMENT_DELETE = None
    object: EventsObjects.MarketCommentDelete = None


class GroupLeave(BaseEvent):
    type: events.Users.GROUP_LEAVE = None
    object: EventsObjects.GroupLeave = None


class GroupJoin(BaseEvent):
    type: events.Users.GROUP_JOIN = None
    object: EventsObjects.GroupJoin = None


class UserBlock(BaseEvent):
    type: events.Users.USER_BLOCK = None
    object: EventsObjects.UserBlock = None


class UserUnblock(BaseEvent):
    type: events.Users.USER_UNBLOCK = None
    object: EventsObjects.UserUnblock = None


class PollVoteNew(BaseEvent):
    type: events.Other.POLL_VOTE_NEW = None
    object: EventsObjects.PollVoteNew = None


class GroupOfficersEdit(BaseEvent):
    type: events.Other.GROUP_OFFICERS_EDIT = None
    object: EventsObjects.GroupOfficersEdit = None


class GroupChangeSettings(BaseEvent):
    type: events.Other.GROUP_CHANGE_SETTINGS = None
    object: EventsObjects.GroupChangeSettings = None


class GroupChangePhoto(BaseEvent):
    type: events.Other.GROUP_CHANGE_PHOTO = None
    object: EventsObjects.GroupChangePhoto = None
