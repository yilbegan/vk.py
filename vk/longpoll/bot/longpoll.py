from vk.utils import mixins
from vk import VK

import logging
import orjson

logger = logging.getLogger(__name__)


# https://vk.com/dev/bots_longpoll


class BotLongPoll(mixins.ContextInstanceMixin):
    def __init__(self, group_id: int, vk: VK):
        """

        :param group_id:
        :param vk:
        """
        self.vk = vk
        self.group_id = group_id
        self.server = None
        self.key = None
        self.ts = None

        self.runned = False

    async def _prepare_longpoll(self):
        """

        :return:
        """
        resp = await self.get_server()
        self.server = resp["server"]
        self.key = resp["key"]
        self.ts = resp["ts"]

        logger.debug(
            f"Prepare polling. Server - {self.server}. Key - {self.key}. TS - {self.ts}"
        )

    async def get_server(self) -> dict:
        """

        :return:
        """
        resp = await self.vk.api_request(
            "groups.getLongPollServer", params={"group_id": self.group_id}
        )
        return resp

    async def get_updates(self, key: str, server: str, ts: str) -> dict:
        """

        :param key:
        :param server:
        :param ts:
        :return:
        """
        async with self.vk.client.post(
            f"{server}?act=a_check&key={key}&ts={ts}&wait=25"
        ) as response:
            resp = await response.json(loads=orjson.loads)
            logger.debug(f"Get updates from polling: {resp['updates']}")
            return resp

    async def listen(self) -> dict:
        """

        :return: 1 event
        """
        updates = await self.get_updates(key=self.key, server=self.server, ts=self.ts)
        self.ts = updates["ts"]
        if updates["updates"]:
            return updates["updates"][0]

    async def run(self) -> dict:
        """

        :return: update coming from VK
        """
        if not self.runned:
            await self._prepare_longpoll()
            self.runned = True
            logger.info("Polling started!")
        while True:
            event = await self.listen()
            if event:
                yield event
