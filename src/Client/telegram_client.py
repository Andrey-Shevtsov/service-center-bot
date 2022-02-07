import os
import json
import requests


class ClientMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance
        return cls._instance[cls]


class Client(metaclass=ClientMeta):
    _telegramId = ""
    _req_address = "https://api.telegram.org/"
    _is_running = False

    def get_token(self):
        cwd = os.getcwd()
        os.chdir("..")
        cfg = open(os.getcwd() + "\src\cfgs\package.json", "r")
        token = json.load(cfg)["bot-token"]
        self._req_address += "bot" + token + "/"
        cfg.close()
        os.chdir(cwd)
        print("request address:" + self._req_address)

    def send_message(self, msg):
        api_string = self._req_address + "sendMessage"
        pass

        # need to get receiver's id
        # there is a problem with replying on messages
        # add start() method (put in await state)

    def long_poll(self):
        api_string = self._req_address + "getUpdates"
        api_params = {"timeout": '60'}
        data = requests.get(api_string, params=api_params)
        return data.text

    def run(self):
        self._is_running = True
        print("Client is now running")

    def stop(self):
        self._is_running = False
        print("Client is no longer running")

    def set_telegram_id(self, tg_id):
        self._telegramId = tg_id

    def get_telegram_id(self):
        return self._telegramId
