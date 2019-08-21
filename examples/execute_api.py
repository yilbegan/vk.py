from vk import VK
from vk.utils import TaskManager

import asyncio
import logging

logging.basicConfig(level="DEBUG")

token = "TOKEN"
vk = VK(access_token=token)
task_manager = TaskManager(vk.loop)


async def status_get():
    a = await vk.execute_api_request("""
    var a = API.status.get();
    return a;
    """)
    print(a)


async def on_startup():
    print("Started!")


async def on_shutdown():
    await vk.close()
    await asyncio.sleep(0.250)
    print("closed!")


if __name__ == "__main__":
    task_manager.add_task(status_get)
    task_manager.run(on_shutdown=on_shutdown, on_startup=on_startup)
    task_manager.close()  # close event loop manually
