from CLI.CMD.CMD import CMD


class CMDfromArray(CMD):

    def __init__(self, commands):
        super().__init__()
        self.__commands = commands

    def run(self):
        for command in self.__commands:
            print(self, end='')
            super().run_command(command)
