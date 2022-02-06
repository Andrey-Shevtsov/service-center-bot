class DeviceFactoryMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class DeviceFactory(metaclass=DeviceFactoryMeta):

    _params = []

    def set_params(self, *args):
        self._params = args

    def get_params(self):
        return self._params

    def create_device(self):
        device = Device(self._params)
        return device

class Device:

    _properties = []

    def __init__(self, *args):
        self._properties = args

