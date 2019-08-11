from vk import VK
from vk.bot_longpoll import BotLongPoll

import asyncio
import logging

logging.basicConfig(level = "DEBUG")
loop = asyncio.get_event_loop()
token = <TOKEN> # bot token

vk = VK(access_token = token, loop = loop)
longpoll = BotLongPoll(group_id = <id>, vk = vk)

async def main():
    async for updates in longpoll.run():
        print(updates)

async def pretty_close():
    await asyncio.sleep(.2)
    await vk.close()


if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(pretty_close())



