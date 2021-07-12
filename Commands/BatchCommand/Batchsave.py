from Commands.BatchCommand.IBatch import IBatch


class Batchsave(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        batch_name = super().find_batch(self.__arguments, '')
        batch = self.__batch_data.get_batch(batch_name)
        file_name = batch_name[1:] if len(self.__arguments) == 1 else self.__arguments[-1]
        if file_name.count(".") > 1:
            raise Exception("error, not valid file name- couldn't contain more that one '.' ")
        if file_name.count(".") == 0:
            file_name += ".rawdna"
        if file_name.split(".")[-1] != "rawdna":
            raise Exception("error, suffix need to be rawdna")

        with open("SavedFile/" + file_name, 'w') as f:
            for command in batch:
                f.write(command + "\n")
        return ''
