from vk import VK
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher, rules
from vk import types
from vk.types.events.community.events_list import Event
import vk.types.events.community.events_objects as eventobj

import asyncio
import logging

logging.basicConfig(level="DEBUG")

bot_token = "token"
vk = VK(bot_token)
gid = 12345
api = vk.get_api()

dp = Dispatcher(vk, gid)


@dp.message_handler(rules.Command("start"))
async def handle(message: types.Message):
    await message.reply("Hello!")


@dp.event_handler(Event.WALL_REPLY_NEW)
async def handle_event(event: eventobj.WallReplyNew):
    print(event)
    # something stuff...


def run():
    dp.run_callback_api("0.0.0.0", 8000, "something..", "/my-bot")


if __name__ == "__main__":
    run()
