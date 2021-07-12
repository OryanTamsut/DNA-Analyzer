from Commands.seqAnalysisCommand.IAnalysisCommand import IAnalysisCommand


class AnalysisFind(IAnalysisCommand):
    def __init__(self , arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        base_seq = super().get_base_seq(self.__arguments, self.__dna_data, "#@")
        str_base_seq = base_seq.get_dna_string()
        seq_to_find = super().get_seq_to_be_found(self.__arguments, self.__dna_data)
        return str(str_base_seq.find(seq_to_find))
