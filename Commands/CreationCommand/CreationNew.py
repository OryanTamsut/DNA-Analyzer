from Commands.CreationCommand.ICreationCommand import ICreationCommand


class CreationNew(ICreationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        Creates a new sequence, as described by the followed sequence.
        If the @<sequence_name> is used, then this will be the name of the new sequence.
        Otherwise, a default name will be provided - seq1 (or seq2 , seq3 and so on, if the
        name is already taken).
        The new sequence, its name and its number (internal ID, starting with 1) are
        printed.
        :return: str that represent the new sequence
        """

        #  find the dna seq to store in it the new string
        new_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, "seq", "")
        new_dna_seq.assignment(self.__arguments[0])
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
