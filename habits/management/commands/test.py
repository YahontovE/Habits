import requests
import time

from django.core.management import BaseCommand

TOKEN = '5401801390:AAEkZjVNHn0HAfhI1gmaPMfQwuuJ5rm_t9Y'
URL = 'https://api.telegram.org/bot'
def get_updates():
    result = requests.get(f'{URL}{TOKEN}/getUpdates?offset=0').json()
    for i in result['result']:
        if 'Яхонтов' in i['message']['from']['last_name']:
            print(i['message']['from']['id'])
        else:
            print(i)

    return result['result']

print(get_updates())