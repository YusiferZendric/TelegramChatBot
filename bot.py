import requests
import json
class telegram_chatbot():
    def __init__(self):
        self.token = "here comes your api token, get it from godfather on telegram"
        self.base = f"https://api.telegram.org/bot{self.token}"
    
    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id, msg)
        print(url)
        if msg is not None:
            requests.get(url)
        
