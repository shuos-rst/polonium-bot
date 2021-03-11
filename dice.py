import numpy as np
import re

#todo get the dice code working with polonium.py

class InputError(Exception):
    pass

def dn(n): #a die with n sides
    return np.random.randint(1,n+1,1)

def xdn(x, n): #x dice with n sides
    if (x < 1) or (n < 1):
        return("numprob")
    dice = np.random.randint(1,n+1,x) #this returns an array
    total = np.sum(dice)
    return("sum: " + str(total) + "\n" + np.array2string(dice, separator=','))

def xdn_ad(x, n): #x dice with n sides, advantage
    if (x < 1) or (n < 1):
        return("numprob")
    dice = np.random.randint(1,n+1,x) #this returns an array
    total = np.sum(dice)
    return("sum: " + str(total) + "\n" + np.array2string(dice, separator=',') + "\n" + "max: " + np.array2string(np.amax(dice))) #np.amax gets the max of the array, but returns that as an array, so we have to convert it to a string

def xdn_da(x, n): #x dice with n sides, disadvantage
    if (x < 1) or (n < 1):
        return("numprob")
    dice = np.random.randint(1,n+1,x) #this returns an array
    total = np.sum(dice)
    return("sum: " + str(total) + "\n" + np.array2string(dice, separator=',') + "\n" + "min: " + np.array2string(np.amin(dice))) #np.amin gets the min of the array, but returns that as an array, so we have to convert it to a string
    
def dice_roll(discord_input, type):
        diceInput = discord_input.partition("d") #returns a tuple with index 0 being the x, index 1 being d, index 2 being the n
        if not re.search(r'^\d*?d\d+$',discord_input):
            return "the vibes are simply rancid"
        n = int(diceInput[2])
        if (not diceInput[0]):
            return (dn(n))
        else:
            x = int(diceInput[0])
            
            if type == 'ad':
                return(xdn_ad(x,n))
            elif type == 'da':
                return(xdn_da(x,n))
            else:
                return (xdn(x,n))


