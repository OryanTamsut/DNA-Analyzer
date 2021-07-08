class Icommand:
    def action(self):
        pass

    def split_command(self, arguments):
        new_arguments = []
        for word in arguments:
            if word != "":
                new_arguments.append(word)
        return new_arguments

    def find_src_seq(self, arguments, dna_data):
        if arguments[0][0] != "@" and arguments[0][0] != "#":
            raise Exception("error, need id or name of the sequence to slice")
        dna_seq = dna_data.get_dna_data(arguments[0])
        if dna_seq is None:
            raise Exception("error, sequence not exist")
        return dna_seq

    def find_target_seq(self, arguments, dna_data, new_name, new_suffix):
        pass
