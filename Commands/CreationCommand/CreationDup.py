from Commands.CreationCommand.ICreationCommand import ICreationCommand


class CreationDup(ICreationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        duplicate sequence
        :return: str that represent the new sequence
        """

        # find the seq to duplicate
        src_seq = super().find_src_seq(self.__arguments, self.__dna_data)

        # find the dna seq to store in it the dna string from the source sequence
        new_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, src_seq.get_name(), "_")
        new_dna_seq.assignment(src_seq)
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
