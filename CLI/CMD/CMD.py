from CLI.CLI import CLI
from Commands.Manage.Invoker import Invoker


class CMD(CLI):

    def __init__(self):
        super().__init__("cmd")
        self.__invoker = Invoker()

    def set_invoker(self, invoker):
        self.__invoker.set_invoker(invoker)

    def run(self):
        pass

    def run_command(self, command):
        if len(command) == 0:
            print("not valid command")
        command = command.strip().split(" ")
        output = self.__invoker.execute(command[0], command[1:])
        if output:
            print(output)
        if command[0] == "quit" and output != "cancel":
            return True
