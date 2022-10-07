from dataclasses import dataclass
from typing import Any, Optional
from services import client
from services.websocket import Controller

@dataclass
class ObjectData:
    module: str
    targets: list[str]
    args: Optional[Any] = None



@client.websocket.on('/bots')
class ControladorController(Controller):
    def on_controlador(self, data):
        objetoData: ObjectData = ObjectData(**data)

        client.manager_main.execute(
            objetoData.module,
            objetoData.args,
            *objetoData.targets
        )