from Commands.Manage.Icommand import Icommand


class IControl(Icommand):
    """
    function to use in Control Commands
    """

    def get_status(self, seq):
        """
        calc the sequence status
        :param seq: to calc
        :return: status
        """

        if seq.get_time_save() == None:
            return "new"
        elif seq.get_time_save() < seq.get_time_update():
            return "modified"
        elif seq.get_time_save() >= seq.get_time_update():
            return "up to date"
