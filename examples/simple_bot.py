from vk import VK
from vk.utils import TaskManager

from vk.bot_framework.dispatcher import Dispatcher
from vk import types

import asyncio
import logging

logging.basicConfig(level="INFO")

token = "TOKEN"
vk = VK(access_token=token)
gid = 123456
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk, gid, mode = "polling")


@dp.message_handler()
async def handle(message: types.Message):
    await api.messages.send(message = message.text, peer_id = message.peer_id)


async def run():
    await dp.run_polling()


async def on_shutdown():
    await vk.close()
    await asyncio.sleep(0.250)
    print("closed!")


if __name__ == "__main__":
    task_manager.add_task(run)
    task_manager.run(on_shutdown=on_shutdown)
