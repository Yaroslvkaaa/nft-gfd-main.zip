'''


в proxyy прокси с новой строки в формате - http://login:pass@ip:port

в keys приватники с новой строки

mode 1 /0  - 1 режим с низким газом через анкррпц / 0 обычный режим

delay - от и до скольки секунд между кошельками

moralis api key - https://admin.moralis.io/login регаемся и получаем апи ключ



'''
import random

with open("keys.txt", "r") as f:
    keys = [row.strip() for row in f]
    random.shuffle(keys)

with open("proxyy.txt", "r") as f:
    proxies = [row.strip() for row in f]

MODE = 1

DELAY = (0, 100)

MORALIS_API_KEY = ''   #https://admin.moralis.io/login