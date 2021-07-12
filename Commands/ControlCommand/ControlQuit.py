from Commands.ControlCommand.IControl import IControl


class ControlQuit(IControl):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        name_to_id, id_to_dna = self.__dna_data.get_all_data()
        count_modified = 0
        count_new = 0
        for name in name_to_id.keys():
            seq = id_to_dna.get(name_to_id[name])
            status = super().get_status(seq)
            if status == "new":
                count_new += 1
            elif status == "modified":
                count_modified += 1
        if count_modified == 0 and count_new == 0:
            return "Thank you for using Dnalanyzer.\nGoodbye!"
        print(f"There are {count_modified} modified and {count_new} new sequences. Are you sure you want to quit?")
        confirm = super().confirm()
        if not confirm:
            return "cancel"
        return "Thank you for using Dnalanyzer.\nGoodbye!"
