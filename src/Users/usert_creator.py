class UserFactoryMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class UserFactory(metaclass=UserFactoryMeta):
    _params = []

    def set_params(self, *params):
        self._params = params

    def get_params(self):
        return self._params

    def create_user(self):
        user = User(self._params)
        return user


class User:

    _properties = []

    def __init__(self, *args):
        self._properties = args

    def execute_command(self, command):
        command.execute()
