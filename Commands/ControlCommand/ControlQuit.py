from Commands.Manage.Icommand import Icommand


class ControlQuit(Icommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        name_to_id, id_to_dna = self.__dna_data.get_all_data()
        count_modifier = 0
        count_new = 0
        for name in name_to_id.keys():
            seq = id_to_dna.get(name_to_id[name])
            if seq.get_time_save() == None:
                count_new += 1
            elif seq.get_time_save() < seq.get_time_update():
                count_modifier += 1
        if count_modifier == 0 and count_new == 0:
            return "Thank you for using Dnalanyzer.\nGoodbye!"
        print(f"There are {count_modifier} modified and {count_new} new sequences. Are you sure you want to quit?\n"
              "Please confirm by 'y' or 'Y' , or cancel by 'n' or 'N' .")
        confirm = input("> confirm >>> ")
        while confirm not in "YyNn" or confirm == "":
            print("You have typed an invalid response. Please either confirm by 'y' / 'Y' , or cancel by 'n' / 'N' .")
            confirm = input("> confirm >>> ")
        if confirm in "Nn":
            return "cancel"
        return "Thank you for using Dnalanyzer.\nGoodbye!"
