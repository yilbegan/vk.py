import sys
import os
import logging

from watchgod import awatch

logger = logging.getLogger(__name__)


def restart():
    os.execv(sys.executable, ["python"] + sys.argv)


async def _auto_reload():
    """
    Coro which see changes in your code and restart him.

    WARNING: unstable work in Windows.
    :return:
    """
    async for _ in awatch("."):
        logging.info("Changes founded. Restarting...")
        restart()
