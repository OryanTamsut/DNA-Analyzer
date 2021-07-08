from Commands.Manage.Icommand import Icommand


class MenageDel(Icommand):
    def __init__(self, dna_data, arguments):
        self.__dna_data = dna_data
        self.__arguments = super().split_command(arguments)

    def action(self):
        src_seq = super().find_src_seq(self.__arguments, self.__dna_data)
        print(f"Do you really want to delete {src_seq.get_name()}: {src_seq.get_short_string()}?\n"
              "Please confirm by 'y' or 'Y' , or cancel by 'n' or 'N' .")
        confirm = input("> confirm >>> ")
        while confirm not in "YyNn" or confirm == "":
            print("You have typed an invalid response. Please either confirm by 'y' / 'Y' , or cancel by 'n' / 'N' .")
            confirm = input("> confirm >>> ")
        if confirm in "Nn":
            return "cancel delete"
        deleted_item = self.__dna_data.delete_dna_seq(src_seq.get_id())
        return f'Deleted: [{deleted_item.get_id()}] {deleted_item.get_name()}: {deleted_item.get_short_string()}'
