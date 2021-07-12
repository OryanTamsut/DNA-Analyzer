from Commands.ControlCommand.IControl import IControl


class ControlShow(IControl):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        sequence = super().find_src_seq(self.__arguments, self.__dna_data)
        if len(self.__arguments) > 2:
            raise Exception("error, not valid number of arguments")
        num_char = int(self.__arguments[1]) if len(self.__arguments) == 2 else 90
        status = super().get_status(sequence)
        seq_represent = f"[{sequence.get_id()}] {sequence.get_name()}, status: {status}\n"
        seq_str = sequence.get_dna_string()[:num_char]
        seq_represent += seq_str
        return seq_represent
