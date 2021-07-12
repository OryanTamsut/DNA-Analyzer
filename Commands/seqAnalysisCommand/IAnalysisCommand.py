from Commands.Manage.Icommand import Icommand


class IAnalysisCommand(Icommand):
    def get_base_seq(self, arguments, dna_data, valid_seq):
        if len(arguments) == 0:
            raise Exception("error, need arguments")
        if arguments[0][0] not in valid_seq:
            raise Exception(
                f"error, the first argument need to start with one of the following: {valid_seq}")
        seq = dna_data.get_dna_data(arguments[0])
        if seq is None:
            raise Exception("error, the seq not found")
        return seq

    def get_seq_to_be_found(self, arguments, dna_data):
        if len(arguments) != 2:
            raise Exception("error, need 2 arguments")
        if arguments[1][0] != "#" and arguments[1][0] != "@":
            return arguments[1]
        seq = dna_data.get_dna_data(arguments[1])
        if seq is None:
            raise Exception("error, the seq not found")
        return seq.get_dna_string()

    def findall(self, base_str, str_to_find):
        arr = []
        for i in range(len(base_str)):
            if base_str[i:].startswith(str_to_find):
                arr.append(i)
        return arr
