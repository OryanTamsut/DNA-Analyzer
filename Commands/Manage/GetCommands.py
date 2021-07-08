from Commands.CreationCommand import CreationLoad, CreationDup, CreationNew


class GetCommands:

    def __init__(self):
        """Factory Method"""
        self.commands = {
            "new": CreationNew.CreationNew,
            "dup": CreationDup.CreationDup,
            "load": CreationLoad.CreationLoad
        }

    def get_command(self, command, dna_data, arguments):
        command = self.commands.get(command)
        if command is None:
            raise ValueError("not valid command")
        return command(dna_data, arguments)
