#command prompt

class command_prompt:

    registry = dict()

    def __init__(self):
        self.registry = dict()

    def add(self, name, command):
        self.registry[name] = command

    def find_and_execute(self, name):
        command_tuple = name.partition(' ')
        #TODO institute a "we didn't find that message"
        return self.registry[command_tuple[0]].execute(command_tuple[2])
