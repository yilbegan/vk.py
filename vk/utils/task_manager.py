import asyncio
import typing

import logging

try:
    import uvloop
except ImportError:
    uvloop = None

from .auto_reload import _auto_reload

logger = logging.getLogger()


class TaskManager:
    """
    Task manager represent to user high-level API of asyncio interface (Less part :))
    """

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.tasks: list = []
        self.loop = loop

    def run(
        self,
        on_shutdown: typing.Callable = None,
        on_startup: typing.Callable = None,
        asyncio_debug_mode: bool = False,
        auto_reload: bool = False,
    ):
        """
        Method which run event loop

        :param auto_reload: auto reload code when changes
        :param on_shutdown: coroutine which runned after complete tasks
        :param on_startup: coroutine which runned before start main tasks
        :param asyncio_debug_mode: asyncio debug mode state
        :return:
        """
        if len(self.tasks) < 1:
            raise RuntimeError("Count of tasks - 0. Add tasks.")
        tasks = [task() for task in self.tasks]
        try:
            if on_startup is not None:
                self.loop.run_until_complete(on_startup())
            tasks = asyncio.gather(*tasks)
            if uvloop:
                uvloop.install()
            logger.info("Loop started!")
            if asyncio_debug_mode:
                self.loop.set_debug(enabled=True)
            if auto_reload:
                self.loop.create_task(_auto_reload())
            self.loop.run_until_complete(tasks)
        finally:
            if on_shutdown is not None:
                self.loop.run_until_complete(on_shutdown())

    def close(self):
        """
        Close event loop manually
        :return:
        """
        self.loop.close()

    def add_task(self, task: typing.Callable):
        """

        Add task to loop when loop don`t started.

        :param task: coroutine for run in loop
        :return:
        """
        if asyncio.iscoroutinefunction(task):
            self.tasks.append(task)
            logger.info(f"Task {task.__name__} successfully added!")
        else:
            raise RuntimeError("Unexpected task. Tasks may be only coroutine")

    def run_task(self, task: typing.Callable):
        """
        Create task in loop

        >> async def other_coro():
            while True:
                print("hello, my friend!")
                await asyncio.sleep(5)

        >> async def my_pretty_coro():
            task_manager.run_task(other_coro)
            return True


        :param task:
        :return:
        """

        self.loop.create_task(task())
