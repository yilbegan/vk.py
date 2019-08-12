from vk import VK

import asyncio
import logging

logging.basicConfig(level = "DEBUG")

token = "TOKEN"
vk = VK(access_token = token)


async def status_get():
    resp = await vk.api_request("status.get")
    print(resp)


async def on_startup():
    print("Started!")


async def on_shutdown():
    await vk.close()
    await asyncio.sleep(0.250)
    print("closed!")

if __name__ == "__main__":
    vk.task_manager.add_task(status_get)
    vk.task_manager.run(on_shutdown = on_shutdown, on_startup = on_startup)
