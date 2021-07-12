from Commands.Manage.GetCommands import GetCommands


class Invoker:
    """command method"""

    def __init__(self):
        self.__factory = GetCommands()

    def set_invoker(self, commands_list):
        self.__factory.set_commands(commands_list)

    def execute(self, command_name, arguments):
        try:
            command = self.__factory.get_command(command_name, arguments)
            output = command.action()
        except Exception as e:
            return str(e)
        return output
