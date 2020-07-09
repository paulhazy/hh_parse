import hh_parse
import config
import requests

hrefs = hh_parse.links
vacancy = hh_parse.get_vacancy

def send_to_tg(str):
    token = config.bot_token
    url = "https://api.telegram.org/bot" + token
    channel_id = '380012573'
    method = url + "/sendMessage"

    req = requests.post(method, data={
        "chat_id": channel_id,
        "text": str
    })


for i in hrefs:
    send_to_tg(vacancy(i, hh_parse.headers))