from abc import ABC, abstractmethod

class AbstractCommand(ABC):

    def __init__(self, command_specific_setup):
        pass

    @abstractmethod
    def execute(self, command_input):
        pass
