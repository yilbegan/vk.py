from ..dispatcher.rule import BaseRule
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


class Text(BaseRule):
    def __init__(self, text: str):
        self.text: str = text

    async def check(self, message: types.Message):
        text = message.text.lower()
        return text == self.text


class Commands(BaseRule):
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
