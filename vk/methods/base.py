from typing import List
import typing


class BaseMethod:
    def __init__(self, vk, category: str):
        self.vk = vk
        self.category = category

    def __str__(self):
        return self.__dict__

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)

    async def api_request(self, method_name: str, params: dict = None):
        return await self.vk._api_request(method_name, params, _raw_mode=True)

    @staticmethod
    def create_params(params):
        """

        :param params:
        :return:
        """
        del params["self"]
        _params = {k: v for k, v in params.items() if v is not None}
        return _params

    @staticmethod
    def list_to_str(obj: List):
        obj = str(obj).strip("[]")
        return obj

    def get_method_name(self, func):
        name = func.__name__

        method_name = ""
        for index, elem in enumerate(name.split("_"), start=1):
            if index == 1:
                method_name += elem
                continue
            method_name += elem.title()

        return self.category + "." + method_name
