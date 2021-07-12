from CLI.CMD.CMD import CMD
from Commands.BatchCommand import RunBatch, CreateBatch, BatchList, Batchshow, Batchsave, Batchload


class CMDfromInput(CMD):
    commands_list = {
        "batch": CreateBatch.CreateBatch,
        "run": RunBatch.RunBatch,
        "batchlist": BatchList.BatchList,
        "batchshow": Batchshow.Batchshow,
        "batchsave": Batchsave.Batchsave,
        "batchload": Batchload.Batchload
    }

    def __init__(self):
        super().__init__()
        super().set_invoker(CMDfromInput.commands_list)

    def run(self):
        print(self, end='')
        command = input()
        while True:
            is_quit = super().run_command(command)
            if is_quit:
                break
            print(self, end='')
            command = input()
