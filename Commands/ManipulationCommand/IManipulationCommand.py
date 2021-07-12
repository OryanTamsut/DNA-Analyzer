from Commands.Manage.Icommand import Icommand


class IManipulationCommand(Icommand):
    def find_target_seq(self, arguments, dna_data, new_name, new_suffix):
        if ":" in arguments:
            colon_index = arguments.index(":")
            if colon_index + 2 != len(arguments):
                raise Exception("error, not valid format, need after colon only one argument")
            if arguments[colon_index + 1][0] != "@":
                raise Exception("error, not valid format- the argument after colon need to start with @")
            if arguments[colon_index + 1] == "@@":
                new_name = dna_data.get_next_name(new_name, new_suffix)
            else:
                new_name = arguments[colon_index + 1]
            return dna_data.add_dna_sec(new_name, "")
        else:
            return super().find_src_seq(arguments, dna_data)

    def find_second_seq(self, dna_data, arguments):
        if arguments[1][0] != "@" and arguments[1][0] != "#":
            raise Exception("error, need id or name of the sequence to slice")
        dna_seq = dna_data.get_dna_data(arguments[1])
        if dna_seq is None:
            raise Exception("error, sequence not exist")
        return dna_seq
