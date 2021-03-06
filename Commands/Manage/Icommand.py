from Data.DnaData import DnaData
from Data.BatchData import BatchData


class Icommand:
    """
    interface for all the commands
    """
    def __init__(self):
        # get database instances
        self.__dna_data = DnaData()
        self.__batch_data = BatchData()

    def action(self):
        pass

    def get_dna_data(self):
        return self.__dna_data

    def get_batch_data(self):
        return self.__batch_data

    def split_command(self, arguments):
        """
        pop out the empty string from arguments array
        :param arguments: the arguments array
        :return: the arguments array without empty strings
        """
        new_arguments = []
        for word in arguments:
            if word != "":
                new_arguments.append(word)
        return new_arguments

    def find_src_seq(self, arguments, dna_data):
        """
        find the DNA sequence on which the action is to be performed
        :param arguments: the command args
        :param dna_data: the database of the dna sequences
        :return: dna sequences
        """
        if arguments[0][0] != "@" and arguments[0][0] != "#":
            raise Exception("error, need id or name of the sequence to slice")
        dna_seq = dna_data.get_dna_data(arguments[0])
        if dna_seq is None:
            raise Exception("error, sequence not exist")
        return dna_seq

    def find_target_seq(self, arguments, dna_data, new_name, new_suffix):
        # find the sequence that store the result
        pass

    def confirm(self):
        """
        confirm the command
        :return: True if confirmed, else- return False
        """
        print("Please confirm by 'y' or 'Y' , or cancel by 'n' or 'N' .")
        confirm = input("> confirm >>> ")
        while confirm not in "YyNn" or confirm == "":
            print("You have typed an invalid response. Please either confirm by 'y' / 'Y' , or cancel by 'n' / 'N' .")
            confirm = input("> confirm >>> ")
        if confirm in "Nn":
            return False
        return True
