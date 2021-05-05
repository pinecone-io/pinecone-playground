from typing import Any
import abc
from ..store import AppStore
from ..effect import AppEffect


class App:
    store: AppStore
    effect: AppEffect


class Page(abc.ABC):
    def __init__(self, app: App):
        self.app = app

    @property
    @abc.abstractmethod
    def title(self):
        raise NotImplementedError

    @abc.abstractmethod
    def render(self):
        raise NotImplementedError
