#this file generates and/or modifies the .env file for the user

import os
from dotenv import load_dotenv, set_key, find_dotenv


def config():
    envpath = find_dotenv()
    if envpath == '':
        newf = open(".env","w+") #creates the new file
        newf.write("# .env\nTOKEN=\nKEYWORD=") #might need to include a newline here
        newf.close()
    load_dotenv()

    #prompt user input for the token and prefix char
    print("welcome to config! this automatically runs on startup, but whenever you want to change settings, delete the .env file and run the bot again \n\nto set up polonium, generate a token from the bot page on the discord developer portal, \nand think up a char that you want to use in front of each command (for example, . or ! or &)")

    token = input("enter token:")
    newkey = input("enter prefix char:")
    wolfram = input("enter wolfram alpha api key (OPTIONAL, just hit enter if you don't want to use this feature): ")


    #set keys/value pairs to new values
    set_key(find_dotenv(),'TOKEN',token)
    set_key(find_dotenv(),'KEYWORD',newkey)
    set_key(find_dotenv(),'WOLFRAM',wolfram)

    #reload the environment with the new values
    load_dotenv(find_dotenv(),stream=None,verbose=False,override=True)

    print("configured with:")
    print("token set to: " + os.getenv('TOKEN'))
    print("prefix char set to: " + os.getenv('KEYWORD'))
    print("wolfram api key set to: " + os.getenv('WOLFRAM'))
