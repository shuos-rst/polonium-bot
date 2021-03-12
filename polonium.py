import os
import discord #https://discordpy.readthedocs.io/en/latest/index.html#
from dotenv import load_dotenv #https://github.com/theskumar/python-dotenv#file-format#
from commands.dice import roll
from commands.randimage import randimage
from config import config
from command_prompt import command_prompt
from commands.callresponse import callresponse, addresponse, deleteresponse
from commands.helpcommand import help

#i wonder if how you would have different versions of the bot for different servers would be having different initializations of the command prompt, and all it's objects.
#the token and shit is all just kinda the gateway to discord, the command_prompt() object is what is handling everything
#theres prob a better way to have the code that actually talks between discord and local computer.


#loading the .env
load_dotenv() #loads the .env file (environment file)
TOKEN = os.getenv('TOKEN') #gets the token from the environment file
KEYWORD= os.getenv('KEYWORD') #sets the keyword for commands
#config the .env on first load
if (TOKEN == ''):
    config()

#this is using the command pattern.
cmnd = command_prompt(KEYWORD) #creates a command prompt

#registering commands to the command prompt
cmnd.add('roll', roll(''), 'where x is the number of dice, and n is the sides of the dice (1d6 for example)')
cmnd.add('rollad', roll('ad'), 'roll with advantage')
cmnd.add('rollda', roll('da'), 'roll with disadvantage')
cmnd.add('woop', randimage('image_csvs/woop_images.csv'), 'sends a random image of wooper')
cmnd.add('miku', randimage('image_csvs/miku_images.csv'), 'sends a random image of hatsune miku')
cmnd.add('hello', callresponse('hello! :)'),'say hello to polonium!')
cmnd.add('gme', callresponse("\U0001F680 to the moon \U0001F680"), "ask polonium about it's opinions about roblox stock")
cmnd.add('rblx', callresponse("\U0001F680 stonks only go up \U0001F680"), "ask polonium about it's opinions about gamestop stock")
cmnd.add('ar', addresponse(cmnd), 'add a custom response to the bot! format: ' + KEYWORD + "addresponse <command> <response> where everything after the space is the response")
cmnd.add('dr', deleteresponse(cmnd), 'delete a custom response. format: ' + KEYWORD + 'dr <' + KEYWORD + 'command>')
cmnd.add('help', help(cmnd), 'prints a list of commands and their descriptions')


#establish connection to discord
client = discord.Client()



#async code that executes on a particular event
    #info about the async/await syntax: https://realpython.com/async-io-python/#

@client.event
async def on_ready(): #prints when the bot connects/reconnects to discord
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith(KEYWORD):
        messageInput = message.content.lstrip(KEYWORD) #strips the KEYWORD prefix from commands
        await message.channel.send(cmnd.find_and_execute(messageInput)) #finds and executes a command from the command prompt

client.run(TOKEN)
