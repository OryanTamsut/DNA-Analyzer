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
            self.__name_to_id = {}
            self.__id_dna = {}
            self.__next_id = 1
            self.__next_name = 0
            DnaData._was_init = True

    def add_dna_sec(self, name, string):
        if name[0] == "@":
            name = name[1:]
        dna_sequence = DnaSequence(name, self.__next_id, string)
        self.__next_id += 1
        self.__name_to_id[dna_sequence.get_name()] = dna_sequence.get_id()
        self.__id_dna[dna_sequence.get_id()] = dna_sequence
        return dna_sequence

    def get_next_name(self, name, suffix):
        if name != "seq" and self.__name_to_id.get(name) is None:
            return name
        num = 1
        while self.__name_to_id.get(name + suffix + str(num)) is not None:
            num += 1
        return name + suffix + str(num)

    def get_dna_data(self, name_or_id):
        if name_or_id[0] == "#":
            try:
                id = int(name_or_id[1:])
            except:
                raise Exception("error, not vaid id number")
            return self.__id_dna.get(id)
        else:
            return self.__id_dna.get(self.__name_to_id.get(name_or_id[1:]))

    def delete_dna_seq(self, id):
        removed = self.__id_dna.pop(id, None)
        if removed is None:
            raise Exception("error, not found this DNA sequence")
        self.__name_to_id.pop(removed.get_name())
        return removed

    def get_all_data(self):
        return self.__name_to_id, self.__id_dna
