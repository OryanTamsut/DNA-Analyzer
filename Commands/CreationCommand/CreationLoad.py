from Commands.CreationCommand.ICreationCommand import ICreationCommand


class CreationLoad(ICreationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        loads the sequence from the file, assigns it with a number (ID) and a default name, if
        one was not provided (based on the file name, possibly postfixed with a number if the
        name already exists), and prints it.
        :return: str that represent the new sequence
        """
        file_name = self.__arguments[0] if "." in self.__arguments[0] else self.__arguments[0] + ".rawdna"
        with open("FilesToLoad/" + file_name, 'r') as f:
            string_dna = f.readline()
        file_name = self.__arguments[0].split(".")[0]
        new_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, file_name, "_")
        new_dna_seq.assignment(string_dna)
        new_dna_seq.set_time_save()
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
