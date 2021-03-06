# from StateMachine import states
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
    offset = 0
    _telegramId = ""
    _req_address = "https://api.telegram.org/"
    is_running = False
    _state = None
    _cfg = None

    def get_token(self):
        cwd = os.getcwd()
        os.chdir("..")
        self._cfg = open(os.getcwd() + "\src\cfgs\package.json", "r")
        token = json.load(self._cfg)["bot-token"]
        self._req_address += "bot" + token + "/"
        self._cfg.close()
        os.chdir(cwd)
        print("request address:" + self._req_address)

    def send_message(self, *args):
        api_string = self._req_address + "sendMessage"
        api_params = {"chat_id": args[0]["id"], "text": args[0]["message"]}
        result = requests.get(api_string, params=api_params)
        return result

        # need to get receiver's id
        # there is a problem with replying on messages
        # add start() method (put in await state)

    def long_poll(self):
        result = {
            "id": "",
            "text": ""
        }
        api_string = self._req_address + "getUpdates"
        if self.offset == 0:
            api_params = {"limit": '1', "timeout": '60'}
        else:
            api_params = {"offset": self.offset, "limit": '1', "timeout": '60'}
        data = requests.get(api_string, params=api_params)
        self.offset = data.json()["result"][0]["update_id"] + 1
        result["id"] = data.json()["result"][0]["message"]["from"]["id"]
        result["text"] = data.json()["result"][0]["message"]["text"]
        return result

    def run(self):
        self.is_running = True
        print("Client is now running")

    def stop(self):
        self.is_running = False
        print("Client is no longer running")

    def set_telegram_id(self, tg_id):
        self._telegramId = tg_id

    def get_telegram_id(self):
        return self._telegramId
