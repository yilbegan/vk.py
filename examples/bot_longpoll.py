from vk import VK
from vk.bot_longpoll import BotLongPoll

import asyncio
import logging

logging.basicConfig(level="INFO")

token = "TOKEN"
vk = VK(access_token=token)
id = "GROUP_ID"
longpoll = BotLongPoll(group_id=id, vk=vk)


async def send_message(obj):
    params = {"random_id": 0, "message": obj["text"], "peer_id": obj["peer_id"]}

    await vk.api_request("messages.send", params)


async def listen_group():
    async for event in longpoll.run():
        print(event)
        if event["type"] == "message_new":
            await send_message(event["object"])


async def on_startup():
    print("Started!")


async def on_shutdown():
    await vk.close()
    await asyncio.sleep(0.250)
    print("closed!")


if __name__ == "__main__":
    vk.task_manager.add_task(listen_group)
    vk.task_manager.run(on_shutdown=on_shutdown, on_startup=on_startup)
