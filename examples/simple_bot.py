from vk import VK
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher, rules
from vk import types
from vk.types.events.community.events_list import Event
import vk.types.events.community.events_objects as eventobj

import asyncio
import logging

logging.basicConfig(level = "INFO")

bot_token = "your_token"
vk = VK(bot_token)
gid = 123
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk, gid)



@dp.message_handler(rules.Command("start"))
async def handle(message: types.Message):
    await message.reply("Hello!")


@dp.event_handler(Event.WALL_REPLY_NEW)
async def handle_event(event: eventobj.WallReplyNew):
    print(event)
    # something stuff...


async def run():
    await dp.run_polling()


if __name__ == "__main__":
    task_manager.add_task(run)
    task_manager.run()
