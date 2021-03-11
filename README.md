# polonium-bot
a low-key discord bot built in python :smile:

## current commands
keyword | description
--------|---------
.help | prints a list of commands and their descriptions
.hello | say hello to polonium!
.roll xdn | where x is the number of dice, and n is the sides of the dice (1d6 for example)
.rollad xdn | roll with advantage
.rollda xdn | roll with disadvantage
.woop | sends a random image of wooper
.miku | sends a random image of hatsune miku
.gme | ask polonium their opinion on gamestop stock
.rblx | ask polonium their opinion on roblox stock

more coming soon!

## using polonium
clone polonium

in the command prompt, change the directory to where polonium.py is. run `python -m pip install -r requirements.txt` to install requirements.

sign into the discord developer portal, and create a new application. go to the bot tab, and click 'add bot'. copy the token from that page.
go to the OAuth2 tab, select "bot" from the scopes pane, and "administrator" from the bot permissions pane. open that link in a new tab to add polonium to a server.

run polonium.py in the command prompt.

the first time the bot is run, it will prompt you to enter the token that you copied earlier and a prefix char (like ! or . or & -- the character that goes in front of each command).

to change the token or prefix char after the first time it's run, delete the file named '.env' and run the bot again
***
[shuos on twitter](https://twitter.com/shuos_)
