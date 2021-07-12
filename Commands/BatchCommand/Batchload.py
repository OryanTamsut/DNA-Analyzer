from Commands.BatchCommand.IBatch import IBatch


class Batchload(IBatch):
    def __init__(self, arguments):
        super().__init__()
        self.__batch_data = super().get_batch_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        file_to_load = self.__arguments[0]
        if file_to_load.count(".") == 0:
            file_to_load += ".rawdna"
        with open("FilesToLoad/" + file_to_load, "r") as f:
            batch = []
            readlines = f.readlines()
            for line in readlines:
                line = line.replace("\n", "")
                batch.append(line)
        batch_name = super().find_target_batch(self.__arguments)
        self.__batch_data.add_batch(batch_name, batch)
        return f"save as {batch_name}"
