from .middleware import MiddlewareManager
from vk.utils import ContextInstanceMixin
from vk import VK

from vk.types.events.community.events_list import Event
from vk.utils.get_event import get_event_object

from .handler import Handler
from vk.longpoll import BotLongPoll

from ..callbackapi import callback_api
from .rule import RuleFactory
from vk.constants import default_rules

import typing
import logging

logger = logging.getLogger(__name__)


class Dispatcher(ContextInstanceMixin):
    def __init__(self, vk: VK, group_id: int):
        self.vk: VK = vk
        self.group_id: int = group_id
        self._hanlders: typing.List[Handler] = []
        self._middleware_manager: MiddlewareManager = MiddlewareManager(self)
        self._rule_factory: RuleFactory = RuleFactory(default_rules())

        self._longpoll: BotLongPoll = BotLongPoll(self.group_id, self.vk)

    def _register_handler(self, handler: Handler):
        """
        Append handler to handlers list
        :param handler:
        :return:
        """
        self._hanlders.append(handler)
        logger.debug(f"Handler '{handler.handler.__name__}' successfully added!")

    def register_message_handler(self, coro: typing.Callable, rules: typing.List):
        """
        Register message handler

        >> dp.register_message_hanlder(my_handler, [])

        :param coro:
        :param rules:
        :return:
        """
        event_type = Event.MESSAGE_NEW
        handler = Handler(event_type, coro, rules)
        self._register_handler(handler)

    def message_handler(self, *rules, **named_rules):
        """
        Register message handler with decorator.

        @dp.message_handler(text="hello")
        async def my_func(msg: types.Message, data: dict):
            print(msg)


        :param rules:
        :param named_rules:
        :return:
        """

        def decorator(coro: typing.Callable):
            nonlocal named_rules
            named_rules = self._rule_factory.get_rules(named_rules)
            self.register_message_handler(coro, named_rules + list(rules))
            return coro

        return decorator

    def register_event_handler(
            self, coro: typing.Callable, event_type: Event, rules: typing.List
    ):
        """
        Register event handler.

        >> dp.register_event_hanlder(my_handler, Event.WallReplyNew, [])

        :param coro:
        :param event_type:
        :param rules:
        :return:
        """
        handler = Handler(event_type, coro, rules=rules)
        self._register_handler(handler)

    def event_handler(self, event_type: Event, *rules, **named_rules):
        """
        Register event handler with decorator.

        @dp.event_handler(Event.WALL_REPLY_NEW)
        async def my_func(event: eventobj.WallReplyNew, data: dict):
            print(event)

        :param event_type:
        :param rules:
        :param named_rules:
        :return:
        """

        def decorator(coro: typing.Callable):
            nonlocal named_rules
            named_rules = self._rule_factory.get_rules(named_rules)
            self.register_event_handler(coro, event_type, named_rules + list(rules))
            return coro

        return decorator

    def setup_middleware(self, middleware):
        """
        Add middleware to middlewares list with middleware manager.
        :param middleware:
        :return:
        """
        self._middleware_manager.setup(middleware)

    def setup_rule(self, rule):
        """
        Add named rule to named rules list with rule factory.
        :param rule:
        :return:
        """
        self._rule_factory.setup(rule)

    async def _process_event(self, event: dict):
        """
        Handle 1 event coming from VK.
        :param event:
        :return:
        """

        data = {}  # dict for transfer data from middlewares to handler.
        # examples/bot_framework/simple_middleware.py

        _skip_handler, data = await self._middleware_manager.trigger_pre_process_middlewares(
            event, data
        )  # trigger pre_process_event funcs in middlewares.
        # returns service value '_skip_handler' and data variable (check upper).

        if not _skip_handler:  # if middlewares don`t skip this handler, dispatcher be check rules and execute handlers.
            ev = await get_event_object(event) # get event pydantic model.
            for handler in self._hanlders: # check handlers
                if handler.event_type.value == ev.type: # if hanlder type is equal event pydantic model.
                    try:
                        result = await handler.execute_handler(ev.object, data) # if execute hanlder func
                        # return non-False value, other handlers doesn`t be executed.
                        if result:
                            break
                    except Exception:
                        logger.exception(
                            f"Error in handler ({handler.handler.__name__}):"
                        )

        await self._middleware_manager.trigger_post_process_middlewares() # trigger post_process_event funcs in middlewares.

    async def _process_events(self, events: typing.List[dict]):
        """
        Process events coming from polling or callback-api.
        :param events: list of events.
        :return:
        """
        for event in events:
            self.vk.loop.create_task(self._process_event(event))

    async def run_polling(self):
        """
        Run polling.
        :return:
        """
        VK.set_current(self.vk)
        await self._longpoll._prepare_longpoll()
        while True:
            events = await self._longpoll.listen()
            if events:
                await self._process_events(events)

    def run_callback_api(self, host: str, port: int, confirmation_code: str, path: str):
        """

        :param host: Host of server. Example: "0.0.0.0"
        :param port: port of server. Example: 8080
        :param confirmation_code: callback api confirmation code. Example: "sdas45643"
        :param path: url where VK send requests. Example: "/my_bot"
        :return:
        """
        app = callback_api.get_app(self, confirmation_code)
        callback_api.run_app(app, host, port, path)
        logger.info("Callback API runned!")
