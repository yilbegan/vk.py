from vk.types.events.community.events_list import Message
from vk.utils import ContextInstanceMixin
from vk import VK

from .handler import Handler, HandlerType
from vk.longpoll import BotLongPoll

import typing
import logging

logger = logging.getLogger(__name__)


class Dispatcher(ContextInstanceMixin):
    def __init__(self, vk: VK, group_id: int, mode: str):
        self.vk: VK = vk
        self.group_id: int = group_id
        self.message_handlers: typing.List[Handler] = []
        self.event_handlers: typing.List[Handler] = []

        self.mode = mode  # polling or callback-api. now support only polling
        if self.mode == "callback":
            raise RuntimeError("Now type 'callback-api' not supported")
        elif self.mode == "longpoll" or self.mode == "polling":
            self.longpoll = BotLongPoll(self.group_id, self.vk)
        else:
            raise RuntimeError("Unsupported type.")


    def register_message_handler(self, coro: typing.Coroutine):
        handler_type = HandlerType.message_handler.value
        handler = Handler(handler_type, coro)
        self.message_handlers.append(handler)


    def message_handler(self):

        def decorator(coro: typing.Coroutine):
            self.register_message_handler(coro)
            return coro

        return decorator


    async def _process_event(self, event: dict):
        _type: str = event["type"]
        if _type == Message.MESSAGE_NEW.value:
            _type = "message_handler"
        else:
            _type = "event_handler"
        if _type == "message_handler":
            for handler in self.message_handlers:
                try:
                    await handler.notify(event)
                except Exception as e:
                    logger.info(f"Error in message handler ({handler.handler.__name__}: {e}")


    async def run_polling(self):
        async for event in self.longpoll.run():
            await self._process_event(event)

