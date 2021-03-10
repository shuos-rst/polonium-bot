import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #this is a thing for the discord token. https://github.com/theskumar/python-dotenv#file-format#
from dice import dice_roll, xdn, dn


#info about the async/await syntax:
    #https://realpython.com/async-io-python/#

load_dotenv() #loads all the files in from the .env file
TOKEN = os.getenv('DISCORD_TOKEN') #gets the token from the .env file

keyword = '.' #this is the keyword for commands

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #TODO is there a better way to handle keyword -> code then this structure? I need to check my 332S book
    elif message.content.startswith(keyword + 'hello'):
        await message.channel.send('Hello!')
        return
    elif message.content.startswith(keyword + 'roll'):
        diceInput = message.content.lstrip('.roll ')
        await message.channel.send(dice_roll(diceInput))
    elif message.content.starswith(keyword + 'gme'):
        await(message.channel.send("\U0001F680 To the moon \U0001F680"))
client.run(TOKEN)