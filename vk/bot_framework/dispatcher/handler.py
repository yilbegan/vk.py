import typing

from enum import Enum
from vk.types.events.community.events_list import Message as m
from vk.types.message import Message

import logging

logger = logging.getLogger(__name__)

class HandlerType(Enum):
    message_handler = "message_handler" # handle messages | return message object
    event_handler = "event_handler" # handel all events | return event object


class Handler:
    def __init__(self, handler_type: str, handler: typing.Callable):
        self.handler_type: str = handler_type  # handler type
        self.handler: typing.Callable = handler

    async def notify(self, event: dict):
        if self.handler_type == "message_handler":
            _message = Message(**event["object"])
            await self.handler(_message)










