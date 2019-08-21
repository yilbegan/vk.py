from ..dispatcher.middleware import BaseMiddleware

from ..dispatcher.middleware import SkipHandler
import time
import logging

logger = logging.getLogger(__name__)

"""
Built-in middlewares.
"""


class SimpleLoggingMiddleware(BaseMiddleware):
    global LAST_TIME
    LAST_TIME = 0

    async def pre_process_event(self, event, data: dict):
        logger.info(f"New event! Type - {event['type']}")
        global LAST_TIME
        LAST_TIME = time.time()
        return data

    async def post_process_event(self):
        result = time.time() - LAST_TIME
        logger.info(f"Handler handled this in {result:.3f} seconds!")
