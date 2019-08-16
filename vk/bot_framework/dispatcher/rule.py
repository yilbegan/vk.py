from abc import ABC, abstractmethod


class AbstractRule(ABC):
    @abstractmethod
    async def check(self, *args):
        """
        This method will be called when rules check.

        :param args:
        :return: True or False. If return 'True' - check next rules or execute handler
        """
        pass


class BaseRule(AbstractRule):
    async def __call__(self, *args):
        return await self.check(*args)
