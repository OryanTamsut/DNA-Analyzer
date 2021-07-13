from Commands.BatchCommand.IBatch import IBatch


class Batchsave(IBatch):
    def __init__(self, arguments):
        super().__init__()
        # get the DB that stores the batch data
        self.__batch_data = super().get_batch_data()
        # split the arguments
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        find batch and save it to file
        :return: '' if sucees
        """
        # find the batch name from the args
        batch_name = super().find_batch(self.__arguments, '')
        batch = self.__batch_data.get_batch(batch_name)
        # find the file name from the args
        file_name = batch_name[1:] if len(self.__arguments) == 1 else self.__arguments[-1]
        if file_name.count(".") > 1:
            raise Exception("error, not valid file name- couldn't contain more that one '.' ")
        if file_name.count(".") == 0:
            file_name += ".rawdna"
        if file_name.split(".")[-1] != "rawdna":
            raise Exception("error, suffix need to be rawdna")

        # save in file
        with open("SavedFile/" + file_name, 'w') as f:
            for command in batch:
                f.write(command + "\n")
        return ''
