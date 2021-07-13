from Commands.CreationCommand import CreationLoad, CreationDup, CreationNew
from Commands.ManipulationCommand import ManipulateSlice, ManipulateReplace, ManipulateConcat
from Commands.SeqMenagmentCommand import MenageDel, MenageSave
from Commands.seqAnalysisCommand import AnalysisLen, AnalysisFind, AnalysisFindall, AnalysisCount
from Commands.ControlCommand import ControlList, ControlQuit, ControlShow


class GetCommands:

    def __init__(self):
        """Factory class"""
        # list of all the commands and their classes
        self.__commands = {
            "new": CreationNew.CreationNew,
            "dup": CreationDup.CreationDup,
            "load": CreationLoad.CreationLoad,
            "slice": ManipulateSlice.ManipulateSlice,
            "replace": ManipulateReplace.ManipulateReplace,
            "del": MenageDel.MenageDel,
            "save": MenageSave.MenageSave,
            "len": AnalysisLen.AnalysisLen,
            "find": AnalysisFind.AnalysisFind,
            "findall": AnalysisFindall.AnalysisFindall,
            "count": AnalysisCount.AnalysisCount,
            "list": ControlList.ControlList,
            "quit": ControlQuit.ControlQuit,
            "show": ControlShow.ControlShow,
            "concat": ManipulateConcat.ManipulateConcat
        }

    def set_commands(self, commands):
        # add commands to the command's list
        self.__commands.update(commands)

    def get_command(self, command, arguments):
        command = self.__commands.get(command)
        if command is None:
            raise ValueError("not valid command")
        return command(arguments)
