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
url = variables['URL']
channel_bot = "habladución"

@client.event
async def on_ready():
    print(f'{client.user} has joined.')


@client.event
async def on_message(message):
    data = str(message.content)
    if message.content.startswith(Prefixes.INFO.value):
        invocador_name = data.replace(Prefixes.INFO.value, "", 1).strip()
        info_player = requests.get(f'{url}/summoner/v4/summoners/by-name/'
                                   f'{invocador_name}?api_key={api_lol}')
        summoner_id = info_player.json()['id']
        # account_id = info_player.json()['accountId']
        # puuid = info_player.json()['puuid']
        basic_info = invocador_name + ' Lvl:' + str(info_player.json()['summonerLevel'])
        print(basic_info)
        info_player2 = requests.get(f'{url}/league/v4/entries/by-summoner/'
                                    f'{summoner_id}?api_key={api_lol}').json()
        for league in info_player2:
            extended_info = league['queueType'] + '->' + league['tier'] + ' ' + league['rank'] + ' - '\
                            + str(league['leaguePoints']) + 'Lp - ' + str(league['wins']) + 'W/'\
                            + str(league['losses']) + 'L -> ' + str(winrate(league['wins'], league['losses']))\
                            + '% Winrate'
            print(extended_info)
        champion_mastery = requests.get(f'{url}/champion-mastery/v4/champion-masteries/'
                                        f'by-summoner/{summoner_id}?api_key={api_lol}').json()
        for champ in champion_mastery[:5]:
            champ_name = Champion.get(champ['championId']).name
            champ_info = champ_name + ' Lvl:' + str(champ['championLevel']) + ' - Points--', str(champ['championPoints'])
            print(champ_info)
        # all_info = basic_info, extended_info
        # await message.channel.send(all_info)

def winrate(wins, losses):
    calculator = round((wins*100)/(losses+wins))
    return calculator


client.run(token)
