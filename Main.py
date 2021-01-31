import discord
import json
from Prefixes import Prefixes
import requests

with open("keys.json") as tempfile:
    variables = json.load(tempfile)
client = discord.Client()
token = variables['token']
prefix = variables['prefix']
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
        print(requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/BrokenSwordParty?api_key=RGAPI-b93a0b44-0bbf-4434-aed6-803f92e2c5ad'))



client.run(token)
