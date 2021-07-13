from Commands.BatchCommand.IBatch import IBatch
from CLI.Batch import Batch


class CreateBatch(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        create a new batch
        """
        # find the batch name from the args
        batch_name = super().find_batch(self.__arguments, '')
        new_batch = Batch()
        # run the batch and save its content in the batch DB
        command_list = new_batch.run()
        self.__batch_data.add_batch(batch_name, command_list)
