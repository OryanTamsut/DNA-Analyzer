from Commands.ControlCommand.IControl import IControl


class ControlList(IControl):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        get the DNA DB and print each dna seq with its status
        :return: string that represent the list of the dna sequences
        """

        name_to_id, id_to_dna = self.__dna_data.get_all_data()
        str = ""
        for name in name_to_id.keys():
            seq = id_to_dna.get(name_to_id[name])
            seq_represent = f"[{seq.get_id()}] {seq.get_name()}: {seq.get_short_string()}"
            if name != list(name_to_id.keys())[-1]:
                seq_represent += "\n"
            status = super().get_status(seq)
            if status == "new":
                str += "o " + seq_represent
            elif status == "modified":
                str += "* " + seq_represent
            else:
                str += "- " + seq_represent
        return str
