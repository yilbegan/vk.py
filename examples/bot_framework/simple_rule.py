from vk import VK
from vk.utils import TaskManager
from vk.bot_framework import Dispatcher, rules
from vk.bot_framework import BaseRule, BaseMiddleware
from vk import types

import logging

logging.basicConfig(level="INFO")

bot_token = "token"
vk = VK(bot_token)
gid = 123
task_manager = TaskManager(vk.loop)
api = vk.get_api()

dp = Dispatcher(vk, gid)


USERS = {}  # schema - id: status


class RegistrationMiddleware(BaseMiddleware):
    """
    Register users in bot.
    """

    async def pre_process_event(self, event, data: dict):
        if event["type"] == "message_new":
            from_id = event["object"]["from_id"]
            if from_id not in USERS:
                USERS[from_id] = "user"
        return data

    async def post_process_event(self):
        pass


class IsAdmin(BaseRule):
    """
    Check admin rights of user.
    """

    def __init__(self, is_admin: bool):
        self.is_admin: bool = is_admin

    async def check(self, message: types.Message):
        status = USERS[message.from_id]
        if not self.is_admin and status != "admin":
            return True
        elif not self.is_admin and status == "admin":
            return False
        elif self.is_admin and status == "admin":
            return True
        elif self.is_admin and status != "admin":
            return False


@dp.message_handler(rules.Command("start"))
async def handle(message: types.Message, data: dict):
    await message.reply("Hello!")


@dp.message_handler(rules.Command("admin"), IsAdmin(True))
async def admin_panel(message: types.Message, data: dict):
    await message.reply("Is admin panel!")


@dp.message_handler(rules.Command("get"), IsAdmin(False))
async def get_admin_rights(message: types.Message, data: dict):
    USERS[message.from_id] = "admin"
    await message.reply("Successfully!")


async def run():
    await dp.run_polling()


if __name__ == "__main__":
    dp.setup_middleware(RegistrationMiddleware())  # setup middleware

    task_manager.add_task(run)
    task_manager.run()
