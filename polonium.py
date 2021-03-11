import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #https://github.com/theskumar/python-dotenv#file-format#
from dice import dice_roll, xdn, dn
from randimage import randimage
from config import config


#loading the .env
load_dotenv() #loads the .env file (environment file)
TOKEN = os.getenv('TOKEN') #gets the token from the environment file
KEYWORD= os.getenv('KEYWORD') #sets the keyword for commands
#config the .env on first load
if (TOKEN == ''):
    config()

#establish connection to discord
client = discord.Client()

#create randimage() objects
woops = randimage('image_csvs/woop_images.csv')
mikus = randimage('image_csvs/miku_images.csv')

#info about the async/await syntax: https://realpython.com/async-io-python/#

#commands
@client.event
async def on_ready(): #prints when the bot connects/reconnects to discord
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #TODO is there a better way to handle keyword -> code then this structure? I need to check my 332S book
        #command pattern -- #https://www.notion.so/shuos/Command-Pattern-595ac1a1e9c842b0a0cdff68e948acfa#

        #ok so. here's how its gonna go down
        #have a command prompt class, with a dictionary with keys being the command, and values being a pointer to the instance of each command
        #have an abstract base class that all command.py files are derived from.
        #have all the command.py files be a class with a constructor and an execute method that returns a string
        #register all command objects to the command prompt like in lab5
            #cp.addCommand("ls", new LSCommand(sfs));# from lab5

        #when a command is entered, we first check if it's got the KEYWORD and not sent by us.
        #then we look it up in the dictionary and execute the command from that pointer.

        #this gets rid of the elifs and makes it OOP


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
