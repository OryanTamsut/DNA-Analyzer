from Commands.CreationCommand import CreationLoad, CreationDup, CreationNew
from Commands.ManipulationCommand import ManipulateSlice, ManipulateReplace
from Commands.SeqMenagmentCommand import MenageDel, MenageSave


class GetCommands:

    def __init__(self):
        """Factory Method"""
        self.commands = {
            "new": CreationNew.CreationNew,
            "dup": CreationDup.CreationDup,
            "load": CreationLoad.CreationLoad,
            "slice": ManipulateSlice.ManipulateSlice,
            "replace": ManipulateReplace.ManipulateReplace,
            "del": MenageDel.MenageDel,
            "save": MenageSave.MenageSave
        }

    def get_command(self, command, dna_data, arguments):
        command = self.commands.get(command)
        if command is None:
            raise ValueError("not valid command")
        return command(dna_data, arguments)
