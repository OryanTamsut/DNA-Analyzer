from Commands.Manage.Icommand import Icommand


class CreationNew(Icommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments = super().split_command(arguments)

    def action(self):
        if len(self.__arguments) == 2:
            if self.__arguments[1][0] != "@":
                return "error, not valid arguments. sequence name start with @"
            new_dna_seq = self.__dna_data.add_dna_sec(self.__arguments[1], self.__arguments[0])
        else:
            new_dna_seq = self.__dna_data.add_dna_sec(self.__dna_data.get_next_name_and_inc(), self.__arguments[0])
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
