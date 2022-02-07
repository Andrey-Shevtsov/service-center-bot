from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass


class AddUser(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        pass


class AddDevice(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        pass


class SearchDevice(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        pass


class ShowDevice(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        pass


class ChangeDevice(Command):

    def __init__(self, payload: str):
        self._payload = payload

    def execute(self) -> None:
        pass
    