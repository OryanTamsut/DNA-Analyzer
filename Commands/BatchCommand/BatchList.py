from Commands.BatchCommand.IBatch import IBatch


class BatchList(IBatch):
    def __init__(self, arguments):
        super().__init__()
        # get the DB that stores the batch data
        self.__batch_data = super().get_batch_data()

        # split the arguments
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        get all the names of batches that stores in batch DB
        :return: string that represents all the batch
        """
        str = ""
        name_list = list(self.__batch_data.get_all_batches().keys())
        for i in range(len(name_list)):
            str += f"[{i}]: {name_list[i]}"
            if i != len(name_list) - 1:
                str += "\n"
        return str
