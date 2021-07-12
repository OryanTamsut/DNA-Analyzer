from Commands.Manage.Icommand import Icommand


class IBatch(Icommand):
    def find_batch(self, arguments, start_with):
        if len(arguments) < 1:
            raise Exception("error, not valid number of arguments, need 2")
        if not arguments[0].startswith(start_with):
            raise Exception(f"error, tha name of batch need to start with {start_with}")
        return arguments[0]

    def find_target_batch(self, arguments):
        if ":" in arguments:
            colon_index = arguments.index(":")
            if colon_index + 2 != len(arguments):
                raise Exception("error, not valid format, need after colon only one argument")
            if arguments[colon_index + 1][0] != "@":
                raise Exception("error, not valid format- the argument after colon need to start with @")
            return arguments[colon_index + 1][1:]
        else:
            return arguments[0].split(".")[0]
