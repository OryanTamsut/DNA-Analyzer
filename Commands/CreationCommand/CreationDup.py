from Commands.Manage.Icommand import Icommand


class CreationDup(Icommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments = super().split_command(arguments)

    def action(self):
        id_or_name = self.__arguments[0]
        if id_or_name[0] != "#":
            return "error, not valid arguments. id start with #"
        dna_seq = self.__dna_data.get_dna_data(id_or_name)
        if dna_seq is None:
            return "error, not found this DNA sequence"
        if len(self.__arguments) == 2:
            if self.__arguments[1][0] != "@":
                return "error, not valid arguments. sequence name start with @"
            new_dna_seq = self.__dna_data.add_dna_sec(self.__arguments[1], dna_seq.get_dna_string())
        else:
            dna_seq.inc_duplicated_item()

            new_dna_seq = self.__dna_data.add_dna_sec(dna_seq.get_name() + "_" + str(dna_seq.get_duplicated_item()),
                                                      dna_seq.get_dna_string())
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
