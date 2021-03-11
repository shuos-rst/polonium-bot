import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #https://github.com/theskumar/python-dotenv#file-format#
from dice import roll, rollad, rollda
from randimage import randimage
from config import config
from command_prompt import command_prompt
from callresponse import callresponse


#loading the .env
load_dotenv() #loads the .env file (environment file)
TOKEN = os.getenv('TOKEN') #gets the token from the environment file
KEYWORD= os.getenv('KEYWORD') #sets the keyword for commands
#config the .env on first load
if (TOKEN == ''):
    config()


cmnd = command_prompt() #creates a command prompt

#registering commands to the command prompt
cmnd.add('roll', roll())
cmnd.add('rollad', rollad())
cmnd.add('rollda', rollda())
cmnd.add('woop', randimage('image_csvs/woop_images.csv'))
cmnd.add('miku', randimage('image_csvs/miku_images.csv'))
cmnd.add('hello', callresponse('hello! :)'))
cmnd.add('rblx', callresponse("\U0001F680 stonks only go up \U0001F680"))
cmnd.add('gme', callresponse("\U0001F680 to the moon \U0001F680"))


#establish connection to discord
client = discord.Client()



#info about the async/await syntax: https://realpython.com/async-io-python/#

#async code that executes on a particular event
@client.event
async def on_ready(): #prints when the bot connects/reconnects to discord
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

        #this gets rid of the elifs and makes it OOP
    elif message.content.startswith(KEYWORD):
        messageInput = message.content.lstrip(KEYWORD)
        await message.channel.send(cmnd.find_and_execute(messageInput))

client.run(TOKEN)

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
