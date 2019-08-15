from vk import VK
from vk.longpoll import BotLongPoll
from vk.utils import TaskManager

import asyncio
import logging

logging.basicConfig(level="INFO")

token = "TOKEN"
vk = VK(access_token=token)
gid = 123456
longpoll = BotLongPoll(group_id=gid, vk=vk)
task_manager = TaskManager(vk.loop)
api = vk.get_api()


async def listen_group():
    async for event in longpoll.run():
        if event["type"] == "message_new":
            await api.messages.send(message = "Hello world!", peer_id = event["object"]["peer_id"])


async def on_startup():
    print("Started!")


async def on_shutdown():
    await vk.close()
    await asyncio.sleep(0.250)
    print("closed!")


if __name__ == "__main__":
    task_manager.add_task(listen_group)
    task_manager.run(on_shutdown=on_shutdown, on_startup=on_startup)
