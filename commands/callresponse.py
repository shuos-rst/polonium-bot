from commands.AbstractCommand import AbstractCommand
from command_prompt import command_prompt
import os
import fileinput

#class that allows us to easily add a call and response style command

class callresponse(AbstractCommand):
    #do a thing where constructing it gives it what to say
    response = str()

    def __init__(self, response):
        self.response = response

    def execute(self, command_input):
        return self.response

class addresponse(AbstractCommand):

    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        newcmnd = command_input.partition(' ')
        if (self.cmnd_prmpt.find_and_execute(str(newcmnd[0])) == 'huh?'):
            if (len(newcmnd[0]) > 15): #we need to make sure command names are < 15 chars, because otherwise you can break .help by adding command names that bring the length of the .help message >2000 characters
                return ("commands with a length of more than 15 characters cannot be added.")
            self.cmnd_prmpt.add(newcmnd[0], callresponse(newcmnd[2]), newcmnd[0])
#TODO finish implementing saveCommand            saveCommand(newcmnd[0], newcmnd[2])
            return('command ' + self.cmnd_prmpt.KEYWORD + newcmnd[0] +" added!")
        else:
            return('that command name is already taken, try again')


class deleteresponse(AbstractCommand):
    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        tobedeleted = command_input.lstrip(self.cmnd_prmpt.KEYWORD)
        if (self.cmnd_prmpt.desc_reg[tobedeleted] == tobedeleted):
            self.cmnd_prmpt.registry.pop(tobedeleted)
            return('command deleted')
        else:
            return('command not found or not allowed to be deleted')


#TODO fully implement
def saveCommand(name, command):
    cmnd_file = open(os.path.join("custom_commands", name + ".txt"),"w+")
    cmnd_file.write(command)
    cmnd_file.close()
    print('command added')

#figure out a way to load all the files from a directory, not just one command
#DO THIS WITH THE CSV LIBRARY
def loadCommand(cmnd_prmpt):
    try:

        f = fileinput.input(files=('TODO get all the files here'))
        command = ''
        for line in f:
            command = command + line
        name = f.filename()
        cmnd_prmpt.add(name, callresponse(command))
    except:
        print('error with loading command')
