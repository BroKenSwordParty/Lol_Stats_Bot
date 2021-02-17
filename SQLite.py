from models.Champions import Champion
import requests
from peewee import *

db = SqliteDatabase('db.sqlite')


def connection():
    db.connect()
    db.create_tables([Champion])


def save_champions():
    db.connect()
    champions_json = requests.get('http://ddragon.leagueoflegends.com/cdn/11.3.1/data/en_US/champion.json').json()
    champions_names = []
    for champion in list(champions_json['data']):
        champions_names.append(champion)
    for champ_name in champions_names:
        name = champions_json['data'][champ_name]['name']
        key = champions_json['data'][champ_name]['key']
        champ = Champion(id=key, name=name)
        print(champ.id, champ.name)
        champ.save()
    db.close()


