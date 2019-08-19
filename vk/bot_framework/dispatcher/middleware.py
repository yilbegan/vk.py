from abc import ABC, abstractmethod
from .handler import SkipHandler

import typing
import logging

logger = logging.getLogger(__name__)


class MiddlewareManager:
    def __init__(self, dispatcher):
        self.dp = dispatcher
        self.middlewares: typing.List[BaseMiddleware] = []

    def setup(self, middleware):
        if not isinstance(middleware, BaseMiddleware):
            raise RuntimeError("Middleware must be only instance of 'BaseMiddleware")

        if middleware.is_configured():
            raise RuntimeError("Middleware already configured!")

        self.middlewares.append(middleware)
        logger.info(f"Middleware '{middleware.__class__.__name__}' successfully added!")

    async def trigger_pre_process_middlewares(self, event, data: dict):
        _skip_handler = False
        for middleware in self.middlewares:
            try:
                data = await middleware.pre_process_event(event, data)
            except SkipHandler:
                logger.debug(
                    f"Middleware {middleware.__class__.__name__} skip handler!"
                )
                _skip_handler = True

        return _skip_handler, data

    async def trigger_post_process_middlewares(self):
        for middleware in self.middlewares:
            await middleware.post_process_event()


class AbstractMiddleware(ABC):
    @abstractmethod
    async def pre_process_event(self, event, data: dict):
        """
        Called before checking filters and execute handler
        :param event:
        :param data:
        :return: data
        """
        pass

    @abstractmethod
    async def post_process_event(self):
        """
        Called after handler
        :return:
        """
        pass


class BaseMiddleware(AbstractMiddleware):
    def __init__(self):
        self._manager = None
        self._configured = False

    def is_configured(self) -> bool:
        return self._configured
