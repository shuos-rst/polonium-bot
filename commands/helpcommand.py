#help command
from commands.AbstractCommand import AbstractCommand
from command_prompt import command_prompt
import os

class help(AbstractCommand):

    def __init__(self, command_prompt_pointer):
        self.cmnd_prmpt = command_prompt_pointer

    def execute(self, command_input):
        #loop through the registry and print all keys
        registry = self.cmnd_prmpt.access_desc_registry()
        commandlist = '```command list:\n'
        for command in registry:
            commandlist +=  self.cmnd_prmpt.KEYWORD + command + "\t" + registry[command] + "\n" \
                if command != 'Custom Commands:' else '\n' + command + "\n"
        commandlist += '```'
        return commandlist
