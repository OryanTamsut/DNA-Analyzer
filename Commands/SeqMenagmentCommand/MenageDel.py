from Commands.Manage.Icommand import Icommand


class MenageDel(Icommand):
    def __init__(self, arguments):
        super().__init__()
        self.__dna_data = super().get_dna_data()
        self.__arguments = super().split_command(arguments)

    def action(self):
        """
        delete command from the DB, ask for confirm
        :return: if success to delete or not
        """
        src_seq = super().find_src_seq(self.__arguments, self.__dna_data)
        confirm = super().confirm()
        if not confirm:
            return "cancel delete"
        deleted_item = self.__dna_data.delete_dna_seq(src_seq.get_id())
        return f'Deleted: [{deleted_item.get_id()}] {deleted_item.get_name()}: {deleted_item.get_short_string()}'
