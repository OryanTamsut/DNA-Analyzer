from Commands.ManipulationCommand.IManipulationCommand import IManipulationCommand


class ManipulateConcat(IManipulationCommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        if len(self.__arguments) < 2:
            raise Exception("error, not valid number of arguments. need <seq_1> <seq_2> arguments")
        new_string = ""
        new_name = ""
        copy_arg = self.__arguments[:]
        dna_seq_1 = super().find_src_seq(self.__arguments, self.__dna_data).get_name()
        for i in range(len(copy_arg)):
            if copy_arg[0] == ":":
                break
            dna_seq = super().find_src_seq(copy_arg, self.__dna_data)
            new_string += dna_seq.get_dna_string()
            if new_name != "":
                new_name += "_" + dna_seq.get_name()
            if len(copy_arg) > 1:
                copy_arg = copy_arg[1:]
        seq_target = super().find_target_seq(self.__arguments, self.__dna_data, dna_seq_1, "_c")
        seq_target.assignment(new_string)
        return f'[{seq_target.get_id()}] {seq_target.get_name()}: {seq_target.get_short_string()}'
