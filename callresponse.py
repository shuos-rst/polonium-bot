#class that allows us to easily add a call and response style command

class callresponse:
    #do a thing where constructing it gives it what to say
    response = str()

    def __init__(self, response):
        self.response = response

    def execute(self, command_input):
        return self.response
