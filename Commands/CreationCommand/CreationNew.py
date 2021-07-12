from Commands.CreationCommand.ICreationCommand import ICreationCommand


class CreationNew(ICreationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        new_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, "seq", "")
        new_dna_seq.assignment(self.__arguments[0])
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
