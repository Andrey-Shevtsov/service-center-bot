from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def show_buttons(self):
        pass


class StartState(State):

    _condition = "start"

    def show_buttons(self):
        pass


class AddUser(State):

    _condition = "addUser"

    def show_buttons(self):
        pass


class AddDevice(State):

    _condition = "addDevice"

    def show_buttons(self):
        pass


class ShowDevices(State):

    _condition = "showDevice"

    def show_buttons(self):
        pass


class SearchDevices(State):

    _condition = "searchDevices"

    def show_buttons(self):
        pass


class AdminState(State):

    _condition = "admin"

    def show_buttons(self):
        pass


class EngineerState(State):

    _condition = "engineer"

    def show_buttons(self):
        pass


class WarehousemanState(State):

    _condition = "warehouseman"

    def show_buttons(self):
        pass


class MyDevices(State):

    _conditions = "myDevices"

    def show_buttons(self):
        pass


class AllDevices(State):

    _condition = "allDevices"

    def show_buttons(self):
        pass


class BySn(State):

    _condition = "bySN"

    def show_buttons(self):
        pass


class ByName(State):

    _condition = "byName"

    def show_buttons(self):
        pass


class ByTimeInterval(State):

    _condition = "byTimeInterval"

    def show_buttons(self):
        pass


class ByStatus(State):

    _condition = "byStatus"

    def show_buttons(self):
        pass
