from socketio import Client
from typing import Type, Callable
from services.websocket import Controller
from pydantic import validate_arguments, BaseModel



class ClientSocket(BaseModel):
    url_connection: str
    namespaces: list[str]
    socket: Client = Client()

    @validate_arguments
    def on(self, event_name: str) -> Callable[[Type[Controller]], None]:
        def wrapper(controller_class: Type[Controller]) -> None:
            self.socket.register_namespace(controller_class(event_name))

        return wrapper

    def start(self) -> None:
        self.socket.connect(self.__url, namespaces=self.__namespaces)
        print(f' CLIENT CONNECT IN {self.__url} '.center(100, '-'))

    def close(self) -> None:
        self.socket.disconnect()
        print(f' CLIENT DISCONNECT IN {self.__url} '.center(100, '-'))
