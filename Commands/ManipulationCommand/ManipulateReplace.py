from Commands.ManipulationCommand.IManipulationCommand import IManipulationCommand


class ManipulateReplace(IManipulationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        replaces the letter in the (0-based) index of <seq> by <new_letter> .
        :return: the string that represent the new DNA seq
        """

        if len(self.__arguments) < 3:
            raise Exception("error, not valid number of arguments. need <seq> <index> <new_letter> arguments")

        dna_seq = super().find_src_seq(self.__arguments, self.__dna_data)
        replaced_str = dna_seq.get_dna_string()
        ind = 1
        # replace the string
        while ind < len(self.__arguments) and self.__arguments[ind] != ":":
            if ind + 1 == len(self.__arguments):
                raise Exception("error, not valid format, need <seq> <index> <new_letter> [: [@<new_seq_name>|@@]]")
            if len(self.__arguments[ind + 1]) > 1:
                raise Exception("error, need letter to replace, not a string")
            index = int(self.__arguments[ind])
            replaced_str = replaced_str[:index] + self.__arguments[ind + 1] + replaced_str[index + 1:]
            ind += 2
        target_dna_seq = super().find_target_seq(self.__arguments, self.__dna_data, dna_seq.get_name(), "_r")
        target_dna_seq.assignment(replaced_str)
        return f'[{target_dna_seq.get_id()}] {target_dna_seq.get_name()}: {target_dna_seq.get_short_string()}'
