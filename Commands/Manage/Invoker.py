from Commands.Manage.GetCommands import GetCommands


class Invoker:
    """command method"""

    def __init__(self):
        self.__factory = GetCommands()

    def execute(self, command_name, dna_data, arguments):
        try:
            command = self.__factory.get_command(command_name, dna_data, arguments)
            output = command.action()
        except (TypeError, ValueError) as e:
            return str(e)
        return output