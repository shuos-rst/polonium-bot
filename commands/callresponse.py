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

class addResponse(AbstractCommand):

    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        newcmnd = command_input.partition(' ')
        if (self.cmnd_prmpt.find_and_execute(str(newcmnd[0])) == 'huh?'):
            if (len(newcmnd[0]) > 15):
                return ("commands with a length of more than 15 characters cannot be added.")
            elif len(newcmnd[0]) < 1:
                return "command name is too short"
            elif len(newcmnd[2]) < 1:
                return "command text is too short"
            self.cmnd_prmpt.add(newcmnd[0], callresponse(newcmnd[2]), newcmnd[0])
#TODO finish implementing saveCommand            saveCommand(newcmnd[0], newcmnd[2])
            return f"command `{self.cmnd_prmpt.KEYWORD}{newcmnd[0]}` added!"
        else:
            return('that command name is already taken, try again')


class deleteResponse(AbstractCommand):
    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        toBeDeleted = command_input.lstrip(self.cmnd_prmpt.KEYWORD)

        if self.cmnd_prmpt.find_and_execute(str(toBeDeleted)) == 'huh?':
            return "that command does not exist"
            
        if self.cmnd_prmpt.desc_reg[toBeDeleted] == toBeDeleted:
            self.cmnd_prmpt.delete(toBeDeleted)
            return f'command `{self.cmnd_prmpt.KEYWORD}{toBeDeleted}` deleted'
        else:
            return('command not allowed to be deleted')


class editResponse(AbstractCommand):

    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        editCommand = command_input.partition(' ')
        if self.cmnd_prmpt.find_and_execute(str(editCommand[0])) == 'huh?':
            return "that command does not exist"
        else:
            if self.cmnd_prmpt.desc_reg[editCommand[0]] == editCommand[0]:
                if len(editCommand[2]) < 1:
                    return "new command text is too short"
                self.cmnd_prmpt.edit(editCommand[0], callresponse(editCommand[2]))
                return f'command `{self.cmnd_prmpt.KEYWORD}{editCommand[0]}` edited'
            else:
                return "that command can't be edited"



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
