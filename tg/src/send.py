#
# Direct send message
#
import os
import requests

user_id = 305707966

token = open(os.path.join(__file__, "../.token")).readline().strip()

data = {"chat_id": user_id, "text": "Проверяю отправку оповещений ботом"}
url = f"https://api.telegram.org/bot{token}/sendMessage"
req = requests.post(url, data)
