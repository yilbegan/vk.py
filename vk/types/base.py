from vk.utils.mixins import ContextInstanceMixin

import pydantic


class BaseModel(pydantic.BaseModel, ContextInstanceMixin):
    class Config:
        allow_mutation = False

    def __str__(self):
        return str(self.dict())

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.dict())

    @property
    def vk(self):
        from vk import VK

        vk = VK.get_current()
        if vk is None:
            raise RuntimeError(
                "Can't get VK instance from context. "
                "You can fix it with setting current instance: "
                "'VK.set_current(vk_instance)'"
            )
        return vk

    @property
    def api(self):
        from vk.methods import API

        api = API.get_current()
        if api is None:
            raise RuntimeError(
                "Can't get API instance from context. "
                "You can fix it with setting current instance: "
                "'API.set_current(API_instance)'"
            )
        return api
