from ..dispatcher.rule import NamedRule, BaseRule
from vk.types.message import Action


from vk import types

import typing

"""
Built-in rules.
"""


class Command(BaseRule):
    def __init__(self, command: str = None):
        self.prefix = "/"
        self.command: str = command

    async def check(self, message: types.Message):
        text = message.text.lower()
        return f"{self.prefix}{self.command}" == text


class Text(NamedRule):

    key = "text"

    def __init__(self, text: str):
        self.text: str = text

    async def check(self, message: types.Message):
        text = message.text.lower()
        return text == self.text


class Commands(NamedRule):

    key = "commands"

    def __init__(self, commands: typing.List[str]):
        self.commands = commands
        self.prefix = "/"

    async def check(self, message: types.Message):
        text = message.text.lower()
        _accepted = False
        for command in self.commands:
            if text == f"{self.prefix}{command}":
                _accepted = True

        return _accepted


class Payload(NamedRule):

    key = "payload"

    def __init__(self, payload: str):
        self.payload = payload

    async def check(self, message: types.Message):
        payload = message.payload
        if payload:
            if payload == self.payload:
                return True


class ChatAction(NamedRule):

    key = "chat_action"

    def __init__(self, action: Action):
        self.action = action

    async def check(self, message: types.Message):
        action = message.action.type
        if action:
            action = Action(action)
            if action is self.action:
                return True



