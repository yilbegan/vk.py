from .middleware import MiddlewareManager
from vk.utils import ContextInstanceMixin
from vk import VK
from vk import types

from .handler import Handler
from vk.longpoll import BotLongPoll

from vk.types.events.community.events_list import Event
from vk.types.events.community import event as eventobj

import typing
import logging

logger = logging.getLogger(__name__)


class Dispatcher(ContextInstanceMixin):
    def __init__(self, vk: VK, group_id: int):
        self.vk: VK = vk
        self.group_id: int = group_id
        self.message_handlers: typing.List[Handler] = []
        self.event_handlers: typing.List[Handler] = []
        self.middleware_manager: MiddlewareManager = MiddlewareManager(self)

        self.longpoll = BotLongPoll(self.group_id, self.vk)

    def register_message_handler(self, coro: typing.Callable, rules: typing.List):
        event_type = Event.MESSAGE_NEW
        handler = Handler(event_type, coro, rules)
        self.message_handlers.append(handler)

    def message_handler(self, *rules):
        def decorator(coro: typing.Callable):
            self.register_message_handler(coro, list(rules))
            return coro

        return decorator


    def register_event_handler(self, coro: typing.Callable, event_type: Event, rules: typing.List):
        handler = Handler(event_type, coro, rules=rules)
        self.event_handlers.append(handler)


    def event_handler(self, event_type: Event, *rules):
        def decorator(coro: typing.Callable):
            self.register_event_handler(coro, event_type, list(rules))
            return coro

        return decorator


    async def _process_event(self, event: dict):
        _skip_handler = await self.middleware_manager.trigger_pre_process_middlewares(
            event
        )
        if not _skip_handler:
            _event_type = Event(event["type"])
            if _event_type is Event.MESSAGE_NEW:
                for handler in self.message_handlers:
                    try:
                        message = types.Message(**event["object"])
                        await handler.execute_handler(message)
                    except Exception as e:
                        logger.error(
                            f"Error in message handler ({handler.handler.__name__.upper()}: {e}"
                        )
            else:
                ev = await self.get_event_object(event)
                for handler in self.event_handlers:
                    if handler.event_type.value == ev.type:
                        try:
                            await handler.execute_handler(ev)
                        except Exception as e:
                            logger.error(
                                f"Error in message handler ({handler.handler.__name__.upper()}: {e}"
                            )

        await self.middleware_manager.trigger_post_process_middlewares()

    async def run_polling(self):
        async for event in self.longpoll.run():
            await self._process_event(event)



    async def get_event_object(self, event):
        _event_type = Event(event["type"])

        if _event_type is Event.MESSAGE_NEW:
            ev = eventobj.MessageNew(**event)

        elif _event_type is Event.MESSAGE_REPLY:
            ev = eventobj.MessageReply(**event)

        elif _event_type is Event.MESSAGE_ALLOW:
            ev = eventobj.MessageAllow(**event)

        elif _event_type is Event.MESSAGES_DENY:
            ev = eventobj.MessageDeny(**event)

        elif _event_type is Event.PHOTO_NEW:
            ev = eventobj.PhotoNew(**event)

        elif _event_type is Event.PHOTO_COMMENT_NEW:
            ev = eventobj.PhotoCommentNew(**event)

        elif _event_type is Event.PHOTO_COMMENT_EDIT:
            ev = eventobj.PhotoCommentEdit(**event)

        elif _event_type is Event.PHOTO_COMMENT_RESTORE:
            ev = eventobj.PhotoCommentRestore(**event)

        elif _event_type is Event.PHOTO_COMMENT_DELETE:
            ev = eventobj.PhotoCommentDelete(**event)

        elif _event_type is Event.AUDIO_NEW:
            ev = eventobj.AudioNew(**event)

        elif _event_type is Event.VIDEO_NEW:
            ev = eventobj.VideoNew(**event)

        elif _event_type is Event.VIDEO_COMMENT_NEW:
            ev = eventobj.VideoCommentNew(**event)

        elif _event_type is Event.VIDEO_COMMENT_EDIT:
            ev = eventobj.VideoCommentEdit(**event)

        elif _event_type is Event.VIDEO_COMMENT_RESTORE:
            ev = eventobj.VideoCommentRestore(**event)

        elif _event_type is Event.VIDEO_COMMENT_DELETE:
            ev = eventobj.VideoCommentDelete(**event)

        elif _event_type is Event.WALL_POST_NEW:
            ev = eventobj.WallPostNew(**event)

        elif _event_type is Event.WALL_REPOST:
            ev = eventobj.WallRepost(**event)

        elif _event_type is Event.WALL_REPLY_NEW:
            ev = eventobj.WallReplyNew(**event)

        elif _event_type is Event.WALL_REPLY_EDIT:
            ev = eventobj.WallReplyEdit(**event)

        elif _event_type is Event.WALL_REPLY_RESTORE:
            ev = eventobj.WallReplyRestore(**event)

        elif _event_type is Event.WALL_REPLY_DELETE:
            ev = eventobj.WallReplyDelete(**event)

        elif _event_type is Event.BOARD_POST_NEW:
            ev = eventobj.BoardPostNew(**event)

        elif _event_type is Event.BOARD_POST_EDIT:
            ev = eventobj.BoardPostEdit(**event)

        elif _event_type is Event.BOARD_POST_RESTORE:
            ev = eventobj.BoardPostRestore(**event)

        elif _event_type is Event.BOARD_POST_DELETE:
            ev = eventobj.BoardPostDelete(**event)

        elif _event_type is Event.MARKET_COMMENT_NEW:
            ev = eventobj.MarketCommentNew(**event)

        elif _event_type is Event.MARKET_COMMENT_EDIT:
            ev = eventobj.MarketCommentEdit(**event)

        elif _event_type is Event.MARKET_COMMENT_RESTORE:
            ev = eventobj.MarketCommentRestore(**event)

        elif _event_type is Event.MARKET_COMMENT_DELETE:
            ev = eventobj.MarketCommentDelete(**event)

        elif _event_type is Event.GROUP_LEAVE:
            ev = eventobj.GroupLeave(**event)

        elif _event_type is Event.GROUP_JOIN:
            ev = eventobj.GroupJoin(**event)

        elif _event_type is Event.USER_BLOCK:
            ev = eventobj.UserBlock(**event)

        elif _event_type is Event.USER_UNBLOCK:
            ev = eventobj.UserUnblock(**event)

        elif _event_type is Event.POLL_VOTE_NEW:
            ev = eventobj.PollVoteNew(**event)

        elif _event_type is Event.GROUP_OFFICERS_EDIT:
            ev = eventobj.GroupOfficersEdit(**event)

        elif _event_type is Event.GROUP_CHANGE_SETTINGS:
            ev = eventobj.GroupChangeSettings(**event)

        elif _event_type is Event.GROUP_CHANGE_PHOTO:
            ev = eventobj.GroupChangePhoto(**event)

        return ev