from ..dispatcher.middleware import BaseMiddleware

from ..dispatcher.middleware import SkipHandler
import logging

logger = logging.getLogger(__name__)


class SimpleLoggingMiddleware(BaseMiddleware):
    async def pre_process_event(self, event):
        logger.info(f"New event! Type - {event['type']}")

    async def post_process_event(self):
        pass
