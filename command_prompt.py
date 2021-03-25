#command prompt

class command_prompt:

    registry = dict() #key/value pair of all the names and pointers to the command objects
    desc_registry = dict() #this is a key/value pair of all the names and the descriptions of what they do
    KEYWORD = '' #the keyword is loaded into the command prompt so that more complicated commands that need to reference the keyword can get it easily, and so that you can create multiple command prompts with different keywords

    def __init__(self, KEYWORD):
        self.registry = dict()
        self.desc_reg = dict()
        self.KEYWORD = KEYWORD

    def add(self, name, command, description):
        self.registry[name] = command
        self.desc_reg[name] = description

    def delete(self, name):
        del self.desc_reg[name]
        del self.registry[name]

    def access_desc_registry(self):
        return self.desc_reg

    def find_and_execute(self, name):
        command_tuple = name.partition(' ')
        try:
            result = self.registry[command_tuple[0]].execute(str(command_tuple[2]))
        except:
            return('huh?') #message for when the command isn't recognized
        return(result)
