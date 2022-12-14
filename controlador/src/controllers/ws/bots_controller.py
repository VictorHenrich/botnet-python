from typing import Type
from start import server
from server.websocket import Controller


@server.websocket.on('/bots')
class BotsController(Controller):
    async def on_connect(self, socketid: str, environ: Type) -> None:
        pass