import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv, find_dotenv #https://github.com/theskumar/python-dotenv#file-format#
from dice import dice_roll, xdn, dn
from randimage import randimage
from config import config

#info about the async/await syntax:
    #https://realpython.com/async-io-python/#
#ODE4OTYzOTgwNjU0NDc3MzUy.YEftpA.tZ4lXaC_YireaxDIV9zSo3ZM2q0


load_dotenv() #loads the .env file (environment file)


TOKEN = os.getenv('TOKEN') #gets the token from the environment file
KEYWORD= os.getenv('KEYWORD') #sets the keyword for commands

if (TOKEN == ''):
    config()

#establish connection to discord
client = discord.Client()

#create randimage() objects
woops = randimage('image_csvs/woop_images.csv')
mikus = randimage('image_csvs/miku_images.csv')


#commands
@client.event
async def on_ready(): #prints when the bot connects/reconnects to discord
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #TODO is there a better way to handle keyword -> code then this structure? I need to check my 332S book

    #TODO implement .help
    #.help command -- COMING SOON -- returns a list of commands
    elif message.content.startswith(KEYWORD + 'help'):
        messageInput = message.content.lstrip('.help ')
        await message.channel.send('coming soon')

    #.hello command -- returns "Hello!"
    elif message.content.startswith(KEYWORD + 'hello'):
        await message.channel.send('hello! :)')

    #.rollad -- standard dice roller, with advantage
    elif message.content.startswith(KEYWORD + 'rollad'):
        messageInput = message.content.lstrip('.rollad ')
        await message.channel.send(dice_roll(messageInput, 'ad'))

    #.rollda -- standard dice roller, with disadvantage
    elif message.content.startswith(KEYWORD + 'rollda'):
        messageInput = message.content.lstrip('.rollda ')
        await message.channel.send(dice_roll(messageInput, 'da'))

    #.roll command -- standard dice roller
    elif message.content.startswith(KEYWORD + 'roll'):
        messageInput = message.content.lstrip('.roll ')
        await message.channel.send(dice_roll(messageInput, ''))

    #.gme command -- returns a message about gamestop stock
    elif message.content.startswith(KEYWORD + 'gme'):
        await(message.channel.send("\U0001F680 to the moon \U0001F680"))

    #.rblx command -- returns a message about roblox stock
    elif message.content.startswith(KEYWORD + 'rblx'):
        await(message.channel.send("\U0001F680 stonks only go up \U0001F680"))

    #.miku command -- returns a link to the miku chug jug song
    elif message.content.startswith(KEYWORD + 'miku'):
        await(message.channel.send(mikus.rand()))

    elif message.content.startswith(KEYWORD + 'woop'):
        await(message.channel.send(woops.rand()))

client.run(TOKEN)
