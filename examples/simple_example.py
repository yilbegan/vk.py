from vk import VK
import asyncio
import logging

logging.basicConfig(level = "INFO")
loop = asyncio.get_event_loop()
token = <TOKEN>

vk = VK(access_token = token, loop = loop)


async def main():
    resp = await vk.api_request(method_name = "status.get")
    print(resp)

async def pretty_close():
    await asyncio.sleep(.2)
    await vk.close()


if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    finally:
        loop.run_until_complete(pretty_close())



