from vk.exceptions.api_errors import APIException

import logging
import asyncio
import typing

logger = logging.getLogger(__name__)

class ExceptionHandler:
    def __init__(self, vk):
        self.vk = vk

    async def _to_many_requests_handle(self, json):
        logger.debug("To many requests exception handle..")
        await asyncio.sleep(.48)
        params = {}
        method_name = None
        for param in json["error"]["request_params"]:
            key = param["key"]
            value = param["value"]
            if key == "method":
                method_name = value
                continue

            params.update({key: value})
        return await self.vk._api_request(method_name = method_name, params = params)


    async def _error_handle(self, json):
        logger.debug("Some exception handle..")
        error = json["error"]

        code: int = error["error_code"]
        if code == 6:  # Too many requests https://vk.com/dev/errors
            return await self._to_many_requests_handle(json)

        msg: typing.AnyStr = error["error_msg"]

        raise APIException(f"[{code}] {msg}")
