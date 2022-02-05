import requests
import json


class TelegramClientMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class TelegramClient(metaclass=TelegramClientMeta):
    _telegramId = ""
    _req_address = "https://api.telegram.org/"

    def __init__(self):
        pass

    def get_token(self):
        cfg = open('../cfgs/package.json')
        token = json.load(cfg)["bot-token"]
        self._req_address += token + "/"

    def send_message(self, msg):
        api_string = self._req_address + "sendMessage"
        pass

        # need to get receiver's id
        # there is a problem with replying on messages
        # add start() method (put in await state)

    def long_poll(self):
        pass