from commands.AbstractCommand import AbstractCommand
from command_prompt import command_prompt

#class that allows us to easily add a call and response style command

class callresponse(AbstractCommand):
    #do a thing where constructing it gives it what to say
    response = str()

    def __init__(self, response):
        self.response = response

    def execute(self, command_input):
        return self.response

#TODO determine a way to save custom commands so that they don't go away on restart
class addresponse(AbstractCommand):

    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        newcmnd = command_input.partition(' ')
        if (self.cmnd_prmpt.find_and_execute(str(newcmnd[0])) == 'huh?'):
            self.cmnd_prmpt.add(newcmnd[0], callresponse(newcmnd[2]), newcmnd[2])
            return('command ' + self.cmnd_prmpt.KEYWORD + newcmnd[0] +" added!")
        else:
            return('that command name is already taken, try again')


class deleteresponse(AbstractCommand):
    def __init__(self, command_prompt_instance):
        self.cmnd_prmpt = command_prompt_instance

    def execute(self, command_input):
        tobedeleted = command_input.lstrip(self.cmnd_prmpt.KEYWORD)
        if (self.cmnd_prmpt.desc_reg[tobedeleted] == self.cmnd_prmpt.registry[tobedeleted].execute('')): #the way to make sure it's a user created command is check to see if the output equals the description (because both are the same *only* with user-created ones)
            self.cmnd_prmpt.registry.pop(tobedeleted)
            return('command deleted')
        else:
            return('command not found or not allowed to be deleted')
