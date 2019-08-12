from .base import BaseMethod
from typing import List

import typing


class Messages(BaseMethod):
    async def add_chat_user(self, chat_id: int, user_id: int):
        """

        :param chat_id:
        :param user_id:
        :return:
        """
        method = self.get_method_name(self.add_chat_user)
        params = self.create_params(locals())
        r = await self.vk.api_request(method, params)
        return r
