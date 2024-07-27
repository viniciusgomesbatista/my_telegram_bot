import requests

class MyTelegramBot:
    def __init__(self):
        self.token = None
        self.chat_id = None

    def set_token(self, token):
        self.token = token
        self.chat_id = self.last_chat_id()
        print("Id do chat:", self.chat_id)

    def last_chat_id(self):
        try:
            url = "https://api.telegram.org/bot{}/getUpdates".format(self.token)
            response = requests.get(url)
            if response.status_code == 200:
                json_msg = response.json()
                for json_result in reversed(json_msg['result']):
                    message_keys = json_result['message'].keys()
                    if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                        return json_result['message']['chat']['id']
                print('Nenhum grupo encontrado')
            else:
                print('A resposta falhou, código de status: {}'.format(response.status_code))
        except Exception as e:
            print("Erro no getUpdates:", e)

    def send_message(self, message):
        try:
            data = {"chat_id": self.chat_id, "text": message}
            url = "https://api.telegram.org/bot{}/sendMessage".format(self.token)
            requests.post(url, data)
        except Exception as e:
            print("Erro no sendMessage:", e)
