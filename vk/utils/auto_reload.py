import sys
import os
import logging

from watchgod import awatch

logger = logging.getLogger(__name__)

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)


async def _auto_reload():
    async for changes in awatch('.'):
        logging.info("Changes founded. Restarting...")
        restart()