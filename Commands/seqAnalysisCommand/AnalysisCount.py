from Commands.seqAnalysisCommand.IAnalysisCommand import IAnalysisCommand


class AnalysisCount(IAnalysisCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        count number of instances of the sub-sequence within the larger sequence.
        :return returns the number of instances of the
        sub-sequence within the larger sequence.
        """
        base_seq = super().get_base_seq(self.__arguments, self.__dna_data, "#@")
        str_base_seq = base_seq.get_dna_string()
        seq_to_find = super().get_seq_to_be_found(self.__arguments, self.__dna_data)
        find = super().findall(str_base_seq, seq_to_find)
        return str(len(find))
