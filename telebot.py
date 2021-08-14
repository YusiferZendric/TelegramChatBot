from requests.sessions import merge_setting
import bot
from chatbot import reply

mybot = bot.telegram_chatbot()


update_id = None


while True:
    # print("...")
    updates = mybot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            myreply = reply(message)
            mybot.send_message(myreply, from_)