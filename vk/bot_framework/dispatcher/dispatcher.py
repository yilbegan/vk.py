from .middleware import MiddlewareManager
from vk.utils import ContextInstanceMixin
from vk import VK
from vk import types

from vk.types.events.community.events_list import Event
from vk.utils.get_event import get_event_object

from .handler import Handler
from vk.longpoll import BotLongPoll

from ..callbackapi import callback_api

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
                        logger.exception(
                            f"Error in message handler ({handler.handler.__name__})"
                        )
            else:
                ev = await get_event_object(event)
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

    def run_callback_api(self, host: str, port: int, confirmation_code: str, path: str):
        """

        :param host: Host string. Example: "0.0.0.0"
        :param port: port
        :param confirmation_code: callback api confirmation code
        :param path: url where VK send requests. Example: "my_bot"
        :return:
        """
        app = callback_api.get_app(self, confirmation_code)
        callback_api.run_app(app, host, port, path)
