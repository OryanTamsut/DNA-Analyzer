from Commands.Manage.Icommand import Icommand


class CreationLoad(Icommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments =  super().split_command(arguments)

    def action(self):
        try:
            with open("FilesToLoad/" + self.__arguments[0], 'r') as f:
                string_dna = f.readline()
        except IOError as e:
            return str(e)
        if len(self.__arguments) == 2:
            if self.__arguments[1][0] != "@":
                return "error, not valid arguments. sequence name start with @"
            new_dna_seq = self.__dna_data.add_dna_sec(self.__arguments[1], string_dna)
        else:
            file_name = self.__arguments[0].split(".")[0]
            check_this_name_exist = self.__dna_data.get_dna_data(file_name)
            if check_this_name_exist is not None:
                check_this_name_exist.inc_duplicated_item()
                new_name = file_name + "_"+str(check_this_name_exist.get_duplicated_item())
                new_dna_seq = self.__dna_data.add_dna_sec(new_name, string_dna)
            else:
                new_dna_seq = self.__dna_data.add_dna_sec(file_name, string_dna)
        return f'[{new_dna_seq.get_id()}] {new_dna_seq.get_name()}: {new_dna_seq.get_short_string()}'
