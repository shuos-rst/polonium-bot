import random
import sys

#todo get the dice code working with polonium.py

class InputError(Exception):
    pass

def dn(n): #a die with n sides
    return random.randrange(1, n+1)

def xdn(x, n): #x dice with n sides
    total = 0
    dice = []
    for i in range(x):
        ret = dn(n)
        total = total + ret
        dice.append(ret)
    string_ints = [str(int) for int in dice] #this creates a new variable string_ints, and initializes it by taking every int in dice and converting it to a string
    return("Sum: " + str(total) + ". Dice: " + ", ".join(string_ints))
    
def dice_roll(discord_input):
    try:
        input = discord_input.partition("d") #returns a tuple with index 0 being the x, index 1 being d, index 2 being the n
        if (input[0] == discord_input): #checks for a failure to partition caused by nonexistent "d"
            raise InputError()
        n = int(input[2])
        if (not input[0]):
            print(dn(n))
        else:
            x = int(input[0])
            return (xdn(x,n))
    
    except:
        return ("Invalid Input.")
#todo: implement edge case handling
    #5. wayy too many dice
    #6. wayy too many dice rolls
