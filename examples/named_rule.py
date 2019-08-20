from vk import VK
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher
from vk.bot_framework.dispatcher.rule import NamedRule
from vk.bot_framework.middlewares import SimpleLoggingMiddleware

from vk import types

import logging

logging.basicConfig(level="INFO")

bot_token = "123"
vk = VK(bot_token)
VK.set_current(vk)
gid = 123
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk, gid)


class Commands(NamedRule):
    key = "commands"

    """
    Own implementaion of commands rule.
    """

    def __init__(self, commands):
        self.commands = commands
        self.prefix = "!"

    async def check(self, message: types.Message):
        text = message.text.lower()
        _accepted = False
        for command in self.commands:
            if text == f"{self.prefix}{command}":
                _accepted = True

        return _accepted


dp.setup_rule(Commands)  # bind


@dp.message_handler(commands=["t"])  # use
async def handle(message: types.Message, data: dict):
    await message.answer("hello!")


async def run():
    await dp.run_polling()


if __name__ == "__main__":
    dp.setup_middleware(SimpleLoggingMiddleware())
    task_manager.add_task(run)
    task_manager.run(auto_reload=True)
