from Commands.Manage.Icommand import Icommand


class MenageSave(Icommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments = super().split_command(arguments)

    def action(self):
        if len(self.__arguments) == 0 or len(self.__arguments) > 2:
            raise Exception("error, not correct format: save <seq> [<filename>]")
        src_seq = super().find_src_seq(self.__arguments, self.__dna_data)
        file_name = src_seq.get_name() if len(self.__arguments) == 1 else self.__arguments[-1]
        if file_name.count(".") > 1:
            raise Exception("error, not valid file name- couldn't contain more that one '.' ")
        if file_name.count(".") == 0:
            file_name += ".rawdna"
        if file_name.split(".")[-1] != "rawdna":
            raise Exception("error, suffix need to be rawdna")

        with open("SavedFile/"+file_name, 'w') as f:
            f.write(src_seq.get_dna_string())
