from vk import VK
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher
from vk import types

import asyncio
import logging

logging.basicConfig(level="INFO")

bot_token = "123"
vk = VK(bot_token)
gid = 123
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk, gid)


@dp.message_handler(commands=["help", "test", "start", "aoff"])
async def handle(message: types.Message):
    await message.reply("Test!")


@dp.message_handler(text="hello")
async def handle_event(message: types.Message):
    await message.reply("Hello!")


async def run():
    await dp.run_polling()


if __name__ == "__main__":
    task_manager.add_task(run)
    task_manager.run()
