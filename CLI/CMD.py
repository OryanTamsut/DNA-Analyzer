from DNAdata.DnaData import DnaData
from CLI.CLI import CLI
from Commands.Manage.Invoker import Invoker


class CMD(CLI):
    def __init__(self):
        super().__init__("cmd")
        self.__dna_data = DnaData()
        self.__invoker = Invoker()

    def run(self):
        print(self, end='')
        command = input()
        while command != "quit":
            if len(command) == 0:
                print("not valid command")
                continue
            command = command.strip().split(" ")
            output = self.__invoker.execute(command[0], self.__dna_data, command[1:])
            if output:
                print(output)
            print(self, end='')
            command = input()
