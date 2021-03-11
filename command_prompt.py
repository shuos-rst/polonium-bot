#command prompt

class command_prompt:

    registry = dict() #key/value pair of all the names and pointers to the command objects
    desc_registry = dict() #this is a key/value pair of all the names and the descriptions of what they do

    def __init__(self):
        self.registry = dict()
        self.desc_reg = dict()

    def add(self, name, command, description):
        self.registry[name] = command
        self.desc_reg[name] = description

    def access_desc_registry(self):
        return self.desc_reg

    def find_and_execute(self, name):
        command_tuple = name.partition(' ')
        try:
            result = self.registry[command_tuple[0]].execute(command_tuple[2])
        except:
            return('huh?') #message for when the command isn't recognized
        return(result)
