from Client import telegram_client

if __name__ == '__main__':
    client = telegram_client.Client()
    client.get_token()
    client.run()
    client.stop()
