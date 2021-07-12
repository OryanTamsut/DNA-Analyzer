from Commands.BatchCommand.IBatch import IBatch
from CLI.Batch import Batch


class CreateBatch(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        batch_name = super().find_batch(self.__arguments, '')
        new_batch = Batch()
        command_list = new_batch.run()
        self.__batch_data.add_batch(batch_name, command_list)
        return
