import discord
import json
from Prefixes import Prefixes
import requests

with open("keys.json") as tempfile:
    variables = json.load(tempfile)
client = discord.Client()
token = variables['token']
prefix = variables['prefix']
api_lol = variables['API_Lol']
channel_bot = "habladución"

@client.event
async def on_ready():
    print(f'{client.user} has joined.')



@client.event
async def on_message(message):
    data = str(message.content)
    print(type(data))
    if message.channel.name == channel_bot and message.content.startswith(prefix):
        print(message.content)
    if message.content.startswith(Prefixes.INFO.value):
        invocador_name = data.replace(Prefixes.INFO.value, "", 1).strip()
        print(invocador_name)
        print(requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
                           f'{invocador_name}?api_key={api_lol}'))
        info_player = requests.get(f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
                                   f'{invocador_name}?api_key={api_lol}')
        summoner_id = info_player.json()['id']
        account_id = info_player.json()['accountId']
        puuid = info_player.json()['puuid']
        print('Nivel: ' + str(info_player.json()['summonerLevel']))
        requests.get(f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
                     f'{summoner_id}?api_key={api_lol}')
        info_player2 = requests.get(f'https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
                                    f'{summoner_id}?api_key={api_lol}').json()
        print(('SoloQ = '), info_player2[0]['tier'], info_player2[0]['rank'], info_player2[0]['leaguePoints'], 'Lp -',
              info_player2[0]['wins'], 'W', info_player2[0]['losses'], 'L -',
              winrate(info_player2[0]['wins'], info_player2[0]['losses']), '% Winrate')
        print(('FlexQ = '), info_player2[1]['tier'], info_player2[1]['rank'], info_player2[1]['leaguePoints'], 'Lp -',
              info_player2[1]['wins'], 'W', info_player2[1]['losses'], 'L -',
              winrate(info_player2[1]['wins'], info_player2[1]['losses']), '% Winrate')

def winrate(wins, losses):
    calculator = round((wins*100)/(losses+wins))
    return calculator

client.run(token)
