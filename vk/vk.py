"""
 MIT License
 
 Copyright (c) 2019 prostomarkeloff
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 
 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.
 
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""

"""
A part of library which represent a main object of VK API.
"""

from vk.constants import API_VERSION, API_LINK

from asyncio import AbstractEventLoop
from aiohttp import ClientSession

from vk.exceptions import APIException

import asyncio
import typing
import orjson

import logging


logger = logging.getLogger(__name__)


class VK:
    def __init__(self, access_token: str, *, loop: AbstractEventLoop = None, client: ClientSession = None):
        self.access_token = access_token
        self.loop = loop if loop is not None else asyncio.get_event_loop()
        self.client = client if client is not None else ClientSession(json_serialize = orjson.dumps)
        self.api_version = API_VERSION

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
        return await self._api_request(method_name = method_name, params = params)

    async def _error_handle(self, json):
        logger.debug("Some exception handle..")
        error = json["error"]

        code: int = error["error_code"]
        if code == 6:  # Too many requests https://vk.com/dev/errors
            return await self._to_many_requests_handle(json)

        msg: typing.AnyStr = error["error_msg"]

        raise APIException(f"[{code}] {msg}")

    async def _api_request(self, method_name: typing.AnyStr, params: dict = None,
                           return_type: str = "json"):
        if params is None or not isinstance(params, dict):
            params = {}

        if not isinstance(return_type, str) or return_type.lower() not in ["json", "object"]:
            logger.warning("Unknown return_type, used 'json'")
            return_type = "json"

        params.update({"v": self.api_version, "access_token": self.access_token})
        async with self.client.post(API_LINK + method_name, params = params) as response:
            if response.status == 200:
                json: typing.Dict = await response.json(loads = orjson.loads)
                logger.debug(f"Response from API: {json}")
                if "error" in json:
                    return await self._error_handle(json)

                if return_type.lower() == "object":
                    logger.warning("Currently return_type 'object' not supported")
                    return json
                return json

    async def api_request(self, method_name, params=None):
        return await self._api_request(method_name = method_name, params = params)

    async def close(self):
        if isinstance(self.client, ClientSession) and not self.client.closed:
            logger.info("Goodbye!")
            await self.client.close()
