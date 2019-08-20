from vk import VK
from vk.bot_framework import Dispatcher
from vk.types.events.community.events_list import Event
import vk.types.events.community.events_objects as eventobj

from vk import types

import logging

logging.basicConfig(level="INFO")

vk = VK("TOKEN")
dp = Dispatcher(vk, 123)


@dp.message_handler(text="start")
async def handle(message: types.Message, data: dict):
    await message.reply("Hello!")


@dp.event_handler(Event.WALL_REPLY_NEW)
async def handle_event(event: eventobj.WallReplyNew, data: dict):
    print(event)
    # something stuff...


def run():
    dp.run_callback_api("0.0.0.0", 8000, "something..", "/my-bot")


if __name__ == "__main__":
    run()
