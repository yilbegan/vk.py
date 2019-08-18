from vk.types.events.community.events_list import Event
from vk.bot_framework.dispatcher.rule import BaseRule
from vk import types

import typing
import logging
import asyncio

logger = logging.getLogger(__name__)


class SkipHandler(Exception):
    pass



class Handler:
    def __init__(
            self, event_type: Event, handler: typing.Callable, rules: typing.List[BaseRule]
    ):
        self.event_type: Event = event_type
        self.handler: typing.Callable = handler
        self.rules: typing.List[BaseRule] = rules

    async def execute_handler(self, *args):
        if self.rules:
            _execute = False
            for rule in self.rules:
                result = await rule(*args)
                if not result:
                    _execute = False
                    break
                _execute = True

            if _execute:
                await self.handler(*args)
        else:
            await self.handler(*args)
