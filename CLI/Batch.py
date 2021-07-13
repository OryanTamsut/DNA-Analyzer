from CLI.CLI import CLI


class Batch(CLI):
    def __init__(self):
        super().__init__("batch")

    def run(self):
        """
        create list of commands
        :return: the list
        """
        print(self, end='')
        command = input()
        command_list = []
        while command != "end":
            command = command.strip()
            command_list.append(command)
            print(self, end='')
            command = input()
        return command_list
