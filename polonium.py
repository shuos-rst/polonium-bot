import os
import discord
    #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #this is a thing for the discord token. 
    #https://realpython.com/how-to-make-a-discord-bot-python/#
    #https://pypi.org/project/python-dotenv/#


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)