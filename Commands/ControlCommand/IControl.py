from Commands.Manage.Icommand import Icommand


class IControl(Icommand):
    def get_status(self, seq):
        if seq.get_time_save() == None:
            return "new"
        elif seq.get_time_save() < seq.get_time_update():
            return "modified"
        elif seq.get_time_save() >= seq.get_time_update():
            return "up to date"
