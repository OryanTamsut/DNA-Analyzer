from Commands.seqAnalysisCommand.IAnalysisCommand import IAnalysisCommand


class AnalysisLen(IAnalysisCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        seq = super().get_base_seq(self.__arguments, self.__dna_data, "#")
        return len(seq)
