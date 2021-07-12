from CLI.CLI import CLI
from Commands.Manage.Invoker import Invoker


class Batch(CLI):
    def __init__(self):
        super().__init__("batch")
        self.__invoker = Invoker()

    def run(self):
        print(self, end='')
        command = input()
        command_list = []
        while command != "end":
            command = command.strip()
            command_list.append(command)
            print(self, end='')
            command = input()
        return command_list
