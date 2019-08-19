from aiohttp import web

import logging
import orjson

logger = logging.getLogger(__name__)


class CallbackAPIHandler(web.View):
    async def get(self):
        raise web.HTTPForbidden()

    async def post(self):
        event = await self.request.json(loads=orjson.loads)
        type = event.get("type")
        if not type:
            raise web.HTTPForbidden()

        if type == "confirmation":
            logger.debug("OK Response sended!")
            return web.Response(text=await self.confirmation_handle())

        else:
            await self.process_event(event)
            logger.debug("OK Response sended!")
            return web.Response(text="ok")

    async def confirmation_handle(self):
        conf_code = self.request.app["confirmation_code"]
        return conf_code

    async def process_event(self, event):
        await self.request.app["dp"]._process_events([event])


def get_app(dp, confirmation_code: str):
    app = web.Application(logger=logger, loop=dp.vk.loop)
    app["confirmation_code"] = confirmation_code
    app["dp"] = dp
    return app


def run_app(app: web.Application, host: str, port: int, path: str):
    app.router.add_view(path, CallbackAPIHandler)
    web.run_app(app, host=host, port=port)
