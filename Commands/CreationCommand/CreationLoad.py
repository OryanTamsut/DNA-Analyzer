from Commands.CreationCommand.ICreationCommand import ICreationCommand


class CreationLoad(ICreationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        file_name = self.__arguments[0] if "." in self.__arguments[0] else self.__arguments[0] + ".rawdna"
        with open("FilesToLoad/" + file_name, 'r') as f:
            string_dna = f.readline()
        file_name = self.__arguments[0].split(".")[0]
        new_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, file_name, "_")
        new_dna_seq.assignment(string_dna)
        new_dna_seq.set_time_save()
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
