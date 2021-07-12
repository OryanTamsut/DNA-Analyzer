from Commands.BatchCommand.IBatch import IBatch
from CLI.CMD.CMDfromArray import CMDfromArray


class RunBatch(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        batch_name = super().find_batch(self.__arguments, '')
        butch = self.__batch_data.get_batch(batch_name)
        cmd = CMDfromArray(butch)
        cmd.run()
        return
