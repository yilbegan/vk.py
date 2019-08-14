from enum import Enum
from ..base import BaseModel

import typing


# https://vk.com/dev/objects/push_settings

class NotificationType(Enum):
    msg = typing.List["on" or "off" or "no_sound" or "no_text"]
    chat = typing.List["on" or "off" or "no_sound" or "no_text"]
    friend = typing.List["on" or "off" or "mutual"]
    friend_found = typing.List["on" or "off"]
    friend_accepted = typing.List["on" or "off"]
    reply = typing.List["on" or "off"]
    comment = typing.List["on" or "off" or "fr_of_fr"]
    mention = typing.List["on" or "off" or "fr_of_fr"]
    like = typing.List["on" or "off" or "fr_of_fr"]
    repost = typing.List["on" or "off" or "fr_of_fr"]
    wall_post = typing.List["on" or "off"]
    wall_publish = typing.List["on" or "off"]
    group_invite = typing.List["on" or "off"]
    group_accepted = typing.List["on" or "off"]
    event_soon = typing.List["on" or "off"]
    tag_photo = typing.List["on" or "off" or "fr_of_fr"]
    app_request = typing.List["on" or "off"]
    sdk_open = typing.List["on" or "off"]
    new_post = typing.List["on" or "off"]
    birthday = typing.List["on" or "off"]


class NotificationSettings(BaseModel):
    msg: NotificationType.msg = None
    chat: NotificationType.chat = None
    friend: NotificationType.friend = None
    friend_found: NotificationType.friend_found = None
    friend_accepted: NotificationType.friend_accepted = None
    reply: NotificationType.reply = None
    comment: NotificationType.comment = None
    mention: NotificationType.mention = None
    like: NotificationType.like = None
    repost: NotificationType.repost = None
    wall_post: NotificationType.wall_post = None
    wall_publish: NotificationType.wall_publish = None
    group_invite: NotificationType.group_invite = None
    group_accepted: NotificationType.group_accepted = None
    event_soon: NotificationType.event_soon = None
    tag_photo: NotificationType.tag_photo = None
    app_request: NotificationType.app_request = None
    sdk_open: NotificationType.sdk_open = None
    new_post: NotificationType.new_post = None
    birthday: NotificationType.birthday = None