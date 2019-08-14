from .base import BaseMethod

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
