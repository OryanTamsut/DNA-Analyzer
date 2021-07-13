from Data.DnaSequence import DnaSequence


class DnaData:
    _instance = None
    _was_init = False

    def __new__(cls, *args, **kwargs):
        if not DnaData._instance:
            DnaData._instance = object.__new__(cls)
        return DnaData._instance

    def __init__(self):
        if not DnaData._was_init:
            # dict that matches every name to ID
            self.__name_to_id = {}

            # dict that matches every ID to DNA seq
            self.__id_dna = {}
            self.__next_id = 1
            DnaData._was_init = True

    def add_dna_sec(self, name, string):
        """
        add new dna seq to the DB
        :param name: the name of the seq
        :param string: the seq string
        :return: the dna sequence that added
        """
        if name[0] == "@":
            name = name[1:]
        dna_sequence = DnaSequence(name, self.__next_id, string)
        self.__next_id += 1
        self.__name_to_id[dna_sequence.get_name()] = dna_sequence.get_id()
        self.__id_dna[dna_sequence.get_id()] = dna_sequence
        return dna_sequence

    def get_next_name(self, name, suffix):
        """
        find the next name: be {name}{suffix}_1 (or {name}{suffix}_2 and so on, if that name is already taken).
        :param name: the name to search if exist
        :param suffix: the suffix to add in the end of the name
        :return: the new name
        """
        if name != "seq" and self.__name_to_id.get(name) is None:
            return name
        num = 1
        while self.__name_to_id.get(name + suffix + str(num)) is not None:
            num += 1
        return name + suffix + str(num)

    def get_dna_data(self, name_or_id):
        """
        get id or name and get the sequence that match to the name or id
        :param name_or_id: name or id to search
        :return: the sequence
        """
        if name_or_id[0] == "#":
            try:
                id = int(name_or_id[1:])
            except:
                raise Exception("error, not vaid id number")
            return self.__id_dna.get(id)
        else:
            return self.__id_dna.get(self.__name_to_id.get(name_or_id[1:]))

    def delete_dna_seq(self, id):
        """
        get id and delete its sequence from the DB
        :param id: id to delete
        :return: the dna that removed
        """
        removed = self.__id_dna.pop(id, None)
        if removed is None:
            raise Exception("error, not found this DNA sequence")
        self.__name_to_id.pop(removed.get_name())
        return removed

    def get_all_data(self):
        return self.__name_to_id, self.__id_dna
