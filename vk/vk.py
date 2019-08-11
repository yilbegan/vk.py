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

from vk.exceptions import APIErrorHandler
from vk.utils.mixins import ContextInstanceMixin

from vk.methods import Messages

import asyncio
import typing
import orjson

import logging

logger = logging.getLogger(__name__)


class VK(ContextInstanceMixin):
    def __init__(self, access_token: str, *, loop: AbstractEventLoop = None, client: ClientSession = None,
                 raw_mode: bool = False):

        """

        :param access_token:
        :param loop:
        :param client:
        :param raw_mode:
        """
        self.access_token = access_token
        self.loop = loop if loop is not None else asyncio.get_event_loop()
        self.client = client if client is not None else ClientSession(json_serialize = orjson.dumps)
        self.api_version = API_VERSION
        self.api_error_handler = APIErrorHandler(self)
        self.raw_mode = raw_mode

        self.messages = Messages(self, category = "messages")


    async def _api_request(self, method_name: typing.AnyStr, params: dict = None):
        """

        :param method_name:
        :param params:
        :return:
        """

        if params is None or not isinstance(params, dict):
            params = {}

        params.update({"v": self.api_version, "access_token": self.access_token})
        async with self.client.post(API_LINK + method_name, params = params) as response:
            if response.status == 200:
                json: typing.Dict = await response.json(loads = orjson.loads)
                logger.debug(f"Response from API: {json}")
                if "error" in json:
                    return await self.api_error_handler.error_handle(json)
                if self.raw_mode:
                    return json

                response = json["response"]
                return response

    async def api_request(self, method_name, params = None) -> dict:
        """

        :param method_name:
        :param params:
        :return:
        """
        return await self._api_request(method_name = method_name, params = params)


    async def close(self):
        """
        :return:
        """
        if isinstance(self.client, ClientSession) and not self.client.closed:
            logger.info("Goodbye!")
            await self.client.close()
