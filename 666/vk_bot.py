

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import requests

token = "vk1.a.Pc4-xQB-VNFHb503SFdIJMwK3uiYcI3luY0HJ9o2pTrRAKfquzvBfGzmaIxFkGyowK66puTh6XKtZUl3P_hwXixrsr2XluSiRjCNKC\
-AAkE0nZ9s5NV3ZQ_v_eKsGcPWDUMBM_J3Uuj5Xa8_vCHmhJBVdeSb3mDDumhZ4ffdNEBkAySSXluVWKLyRfXH3mf1pvFGsJZa7vJTpgDkoc2-kQ"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def get_starships():
    url="https://swapi.dev/api/starships/"
    response = requests.get(url)
    data = response.json()
    largest_speed = data["results"][0]
    for starship in data["results"]:
        if starship["max_atmosphering_speed"] > largest_speed["max_atmosphering_speed"]:
            largest_speed = starship
    return largest_speed["name"]

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 9999999)
        if msg == 'корабли':
            response = f'Самая большая скорость у корабля - {get_starships()}'
        else:
            response = "Неизвестная команда"
        vk.messages.send(peer_id=user_id, random_id=random_id, message=response)



