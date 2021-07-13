from Commands.ControlCommand.IControl import IControl


class ControlShow(IControl):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        Shows the sequence: Its ID, its name, its status and the sequence itself.
        The status is either up to date (was not changed since last save), modified
        (changed since last save) or new (not yet connected to a file).
        The ID, name and status are printed in the first line.
        Then, the sequence itself is printed in the next lines, no more than 99 chars per line.
        If <num_chars> is provided, then this is the number of chars to print (if the sequence
        is longer than that). Otherwise, <num_chars> defaults to 99.
        :return: str that represent the sequence
        """

        sequence = super().find_src_seq(self.__arguments, self.__dna_data)
        if len(self.__arguments) > 2:
            raise Exception("error, not valid number of arguments")
        num_char = int(self.__arguments[1]) if len(self.__arguments) == 2 else 90
        status = super().get_status(sequence)
        seq_represent = f"[{sequence.get_id()}] {sequence.get_name()}, status: {status}\n"
        seq_str = sequence.get_dna_string()[:num_char]
        seq_represent += seq_str
        return seq_represent
