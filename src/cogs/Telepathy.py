import server
from aiohttp import web
from discord.ext import commands
from aiohttp.web_request import Request


class Telepathy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.server = server.HTTPServer(
            bot=self.bot,
            host="0.0.0.0",
            port=8000,
        )
        self.bot.loop.create_task(self._start_server())

    async def _start_server(self):
        await self.bot.wait_until_ready()
        await self.server.start()

    @server.add_route(path="/telepathy", method="POST", cog="Telepathy")
    async def telepathy(self, request: Request):
        if not request.body_exists:
            return web.json_response("You need to provide the \"telepathy\" text data in body", status=400)
        data = await request.post()
        if not data.get("telepathy"):
            return web.json_response("You need to provide the \"telepathy\" text data in body", status=400)
        await self.bot.get_channel(1085229693084651613).send(data.get("telepathy"))
        return web.json_response(status=200)