from .base import BaseMethod
from typing import List

from vk.types.responses import SimpleResponse, ItemsResponse
from vk.types.user import User

import typing

class Account(BaseMethod):

    async def ban(self, owner_id: int):
        """

        :param owner_id:
        :return:
        """
        method = self.get_method_name(self.ban)
        params = self.create_params(locals())
        r = await self.api_request(method, params)
        return SimpleResponse(**r)
