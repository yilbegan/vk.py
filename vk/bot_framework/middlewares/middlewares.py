from ..dispatcher.middleware import BaseMiddleware

from ..dispatcher.middleware import SkipHandler
import time
import logging

logger = logging.getLogger(__name__)

"""
Built-in middlewares.
"""


class SimpleLoggingMiddleware(BaseMiddleware):
    global LAST_TIME_
    LAST_TIME_ = 0

    async def pre_process_event(self, event, data: dict):
        logger.info(f"New event! Type - {event['type']}")
        global LAST_TIME_
        LAST_TIME_ = time.time()
        return data

    async def post_process_event(self):
        result = time.time() - LAST_TIME_
        logger.info(f"Handler handled this in {result:.3f} seconds!")
