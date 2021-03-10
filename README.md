# polonium-bot
a low-key discord bot built using discord.py, numpy, and python-dotenv

## current commands
keyword | description
--------|---------
.hello |
.roll xdn | where x is the number of dice, and n is the sides of the dice (1d6 for example)
.rollad xdn | roll with advantage
.rollda xdn | roll with disadvantage
.gme |

more coming soon!

## configuring for a server
to get polonium to work, you need to add a .env file to configure it. create a file named ".env". the contents of the file should be the below code, with the token from the discord developer portal pasted directly after DISCORD_TOKEN=
```python
# .env
DISCORD_TOKEN=
```
[shuos on twitter](https://twitter.com/home)
