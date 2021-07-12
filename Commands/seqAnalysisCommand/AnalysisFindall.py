from Commands.seqAnalysisCommand.IAnalysisCommand import IAnalysisCommand


class AnalysisFindall(IAnalysisCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        base_seq = super().get_base_seq(self.__arguments, self.__dna_data, "#@")
        str_base_seq = base_seq.get_dna_string()
        seq_to_find = super().get_seq_to_be_found(self.__arguments, self.__dna_data)
        found = super().findall(str_base_seq, seq_to_find)
        str_to_ret = ""
        for i in found:
            str_to_ret += str(i) + " "
        return str_to_ret


