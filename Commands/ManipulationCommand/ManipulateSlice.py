from Commands.ManipulationCommand.IManipulationCommand import IManipulationCommand


class ManipulateSlice(IManipulationCommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments = super().split_command(arguments)

    def menage_arguments(self):
        try:
            from_ind = int(self.__arguments[1])
            last_ind = int(self.__arguments[2])
        except:
            raise Exception("error, from index and to index need be integers")
        if len(self.__arguments) != 3 and len(self.__arguments) != 5:
            raise Exception("error, not valid command, need <seq> <from_ind> <to_ind> [: [@<new_seq_name>|@@]] format")
        return from_ind, last_ind

    def action(self):
        is_valid = self.menage_arguments()
        from_ind = is_valid[0]
        last_ind = is_valid[1]
        dna_seq = super().find_src_seq(self.__arguments, self.__dna_data)
        dna_seq_str_new = dna_seq.get_dna_string()[from_ind:last_ind]
        target_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, dna_seq.get_name(), "_s")
        target_dna_seq.assignment(dna_seq_str_new)
        return f'[{target_dna_seq.get_id()}] {target_dna_seq.get_name()}: {target_dna_seq.get_short_string()}'
