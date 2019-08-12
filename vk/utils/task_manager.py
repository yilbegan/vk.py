import asyncio
import typing

import logging
import uvloop

logger = logging.getLogger()


class TaskManager:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.tasks = []
        self.loop = loop


    def run(self, on_shutdown: typing.Callable = None, on_startup: typing.Callable = None):
        """
        This method run loop.
        :return:
        """
        if len(self.tasks) < 1:
            raise RuntimeError("Count of tasks - 0. Add tasks.")
        tasks = [task() for task in self.tasks]
        try:
            if on_startup is not None:
                self.loop.run_until_complete(on_startup())
            tasks = asyncio.gather(*tasks)
            uvloop.install()
            logger.info("Loop started!")
            self.loop.run_until_complete(tasks)
        finally:
            if on_shutdown is not None:
                self.loop.run_until_complete(on_shutdown())
            logger.info("Loop closed!")
            self.loop.close()


    def add_task(self, task: typing.Callable):
        """

        :param task:
        :return:
        """
        if asyncio.iscoroutinefunction(task):
            self.tasks.append(task)
            logger.info(f"Task {task.__name__.upper()} successfully added!")
        else:
            raise RuntimeError("Unexpected task. Tasks may be only coroutine")