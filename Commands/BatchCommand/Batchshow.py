from Commands.BatchCommand.IBatch import IBatch


class Batchshow(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        batch_name = super().find_batch(self.__arguments, "@")
        batch = self.__batch_data.get_batch(batch_name)
        str = ""
        for command in batch:
            str += command
            if command != batch[-1]:
                str += "\n"
        return str
