from ..dispatcher.rule import BaseRule
from vk import types

import typing


class Command(BaseRule):
    def __init__(self, command: str, prefixes: typing.List[str] = None):
        if not prefixes:
            self.prefixes = ["/"]
        else:
            self.prefixes = prefixes
        self.command: str = command

    async def check(self, message: types.Message):
        text = message.text.lower()

        for prefix in self.prefixes:
            return f"{prefix}{self.command}" == text


class Text(BaseRule):
    def __init__(self, text: str):
        self.text: str = text

    async def check(self, message: types.Message):
        text = message.text.lower()

        return text == self.text
