from __future__ import annotations
from typing import Any, Mapping, Sequence
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
from dataclasses import dataclass
from abc import ABC, abstractmethod
from . import AbstractDOMSelection, AbstractDOMOperation


@dataclass
class DOMSelector:
    type: AbstractDOMSelection
    value: str


@dataclass
class DOMOperator:
    type: AbstractDOMOperation
    param: Any


class AbstractDOM(ABC):
    @abstractmethod
    def active(self, *args: Sequence[Any], kwargs: Mapping[str, Any]) -> None:
        pass


@dataclass
class DOM(AbstractDOM):
    webdriver: WebDriver
    selector: DOMSelector
    operator: DOMOperator
    wait_time: float = 0

    def active(self) -> None:
        element: WebElement = self.selector.type.get_by(
            self.webdriver, self.selector.value
        )

        self.operator.type.start(self.webdriver, element, self.operator.param)

        sleep(self.wait_time)
