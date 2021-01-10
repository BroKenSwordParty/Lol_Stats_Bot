import discord
import json

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
    if message.channel.name == channel_bot and message.content.startswith(prefix):
        print(message.content)


client.run(token)
