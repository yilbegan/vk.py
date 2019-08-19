from abc import ABC, abstractmethod

import logging

logger = logging.getLogger(__name__)


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
        logger.debug(f"Rule {self.__class__.__name__} succesfully called!")
        return await self.check(*args)


class NamedRule(BaseRule):
    """
    May be added to rules with RuleFactory and
    called in handlers by unique key;

    @dp.message_handler(unique_key = value)

    """

    key = None  # unique value for access to rule in handlers.


class RuleFactory:
    def __init__(self, config: dict):
        self.config = config  # dict of all known rules

    def setup(self, rule: NamedRule):
        if not issubclass(rule, NamedRule):
            raise RuntimeError("Only NamedRules may be added in rule factory!")

        if rule.key is None:
            raise RuntimeError("Unallowed key for rule")

        self.config.update({rule.key: rule})
        logger.debug(f"Rule {rule.__class__.__name__} succesfully added!")

    def get_rules(self, user_rules: dict):
        rules = []
        for key, value in user_rules.items():
            if key in self.config:
                rules.append(self.config[key](value))
                continue
            else:
                raise RuntimeError(f"Unknown rule passed: {key}")

        return rules
