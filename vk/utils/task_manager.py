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
    Task manager which present to user high-level API of asyncio operations (Less part :))
    """

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.tasks: list = []
        self.loop = loop

        self.lock: bool = False  # For raise Exceptions when user want add tasks to running loop.

    def run(
        self,
        on_shutdown: typing.Callable = None,
        on_startup: typing.Callable = None,
        asyncio_debug_mode: bool = False,
        auto_reload: bool = False,
    ):
        """
        Method which run event loop

        :param on_shutdown: coroutine which runned after complete tasks
        :param on_startup: coroutine which runned before run main tasks
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
            self.lock = True
            if auto_reload:
                self.loop.create_task(_auto_reload())
            self.loop.run_until_complete(tasks)
        finally:
            if on_shutdown is not None:
                self.loop.run_until_complete(on_shutdown())
            self.lock = False

    def close(self):
        """
        Close event loop
        :return:
        """
        self.loop.close()
    def add_task(self, task: typing.Callable):
        """

        Add task to loop when loop don`t started.

        :param task: coroutine for run in loop
        :return:
        """
        if not self.lock:
            if asyncio.iscoroutinefunction(task):
                self.tasks.append(task)
                logger.info(f"Task {task.__name__.upper()} successfully added!")
            else:
                raise RuntimeError("Unexpected task. Tasks may be only coroutine")
        else:
            raise RuntimeError("Loop already running. Adding tasks is impossible")

    def run_task(self, task: typing.Callable):
        """
        Add task to running loop
        :param task:
        :return:
        """

        self.loop.create_task(task())
