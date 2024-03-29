from aiohttp.web import Application, RouteTableDef, run_app
from typing import Sequence, Union

from utils.types import DictType


class HttpServer:
    __props_run_server: Sequence[str] = "host", "port"

    def __init__(
        self, host: str, port: Union[int, str], secret_key: str, debug: bool = False
    ) -> None:
        self.__configs: DictType = {
            "host": host,
            "port": port,
            "secret_key": secret_key,
        }

        self.__app: Application = Application(debug=debug)

        self.__routes: RouteTableDef = RouteTableDef()

    @property
    def configs(self) -> DictType:
        return self.__configs

    @property
    def app(self) -> Application:
        return self.__app

    @property
    def routes(self) -> RouteTableDef:
        return self.__routes

    def start(self) -> None:
        self.__app.add_routes(self.__routes)

        c: DictType = {
            prop: value
            for prop, value in self.__configs.items()
            if prop in HttpServer.__props_run_server
        }

        run_app(self.__app, **c)
