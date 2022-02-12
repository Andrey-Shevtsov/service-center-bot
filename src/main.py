from Client import telegram_client

if __name__ == '__main__':
    data = None
    i = 0
    client = telegram_client.Client()
    client.get_token()
    client.run()
    while client.is_running:
        if data is None:
            data = client.long_poll()
            i += 1
            print("iter: " + str(i))
            print("offset: " + str(client.offset))
        else:
            print(data)
            reply = {
                "id": data["id"],
                "message": "ping"
            }
            client.send_message(reply)
            data = None
            if i == 5:
                client.stop()
