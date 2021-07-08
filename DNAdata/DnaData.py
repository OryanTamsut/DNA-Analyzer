from DNAdata.DnaSequence import DnaSequence


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
            self.__next_id = 0
            self.__next_name = 0
            DnaData._was_init = True

    def add_dna_sec(self, name, string):
        self.__next_id += 1
        if name[0] == "@":
            name = name[1:]
        dna_sequence = DnaSequence(name, self.__next_id, string)
        self.__name_to_id[dna_sequence.get_name()] = dna_sequence.get_id()
        self.__id_dna[dna_sequence.get_id()] = dna_sequence
        return dna_sequence

    def get_next_id_and_inc(self):
        self.__next_id += 1
        return self.__next_id

    def get_next_name_and_inc(self):
        self.__next_name += 1
        return "seq" + str(self.__next_name)

    def get_dna_data(self, name_or_id):
        if name_or_id[0] == "#":
            return self.__id_dna.get(int(name_or_id[1:]))
        else:
            return self.__id_dna[self.__name_to_id.get(name_or_id[1:])]
