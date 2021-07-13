from Commands.Manage.Icommand import Icommand


class ICreationCommand(Icommand):
    """
    function that uses in Creation Command
    """

    def find_target_seq(self, arguments, dna_data, new_name, new_suffix):
        """
        find the sequence to store in it the command result
        :param arguments: command's arguments
        :param dna_data: the DNA DB
        :param new_name: the new name of the dna sequence if not receive a specific name
        :param new_suffix: the suffix for the new name
        :return: the dna
        """
        if len(arguments) == 2:
            if arguments[1][0] != "@":
                raise Exception("error, not valid arguments. sequence name start with @")
            new_name = arguments[1]
        elif len(arguments) == 0:
            raise Exception("error, need arguments")
        else:
            new_name = dna_data.get_next_name(new_name, new_suffix)
        return dna_data.add_dna_sec(new_name, "")
