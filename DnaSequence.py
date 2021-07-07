class DnaSequence:
    def __init__(self, string):
        if type(string) is str:
            for i in string:
                if i not in "ACTG":
                    raise ValueError
            self.__dna_string = string
        else:
            self.__dna_string = ""

    def insert(self, nucleotide_value, index):
        if type(nucleotide_value) is not str or len(nucleotide_value) > 1 or nucleotide_value not in "ACTG":
            raise TypeError
        if 0 <= index < len(self.__dna_string):
            self.__dna_string = self.__dna_string[:index] + nucleotide_value + self.__dna_string[index:]
        elif index == len(self.__dna_string):
            self.__dna_string += nucleotide_value
        else:
            raise IndexError

    def get_dna_string(self):
        return self.__dna_string

    def assignment(self, new_dna):
        if type(new_dna) is str:
            self.__dna_string = new_dna
        elif type(new_dna) is DnaSequence:
            self.__dna_string = new_dna.__dna_string
        else:
            raise TypeError

    def __str__(self):
        return self.__dna_string

    def __eq__(self, other):
        return type(self) == type(other) and self.__dna_string == other.__dna_string

    def __ne__(self, other):
        return not self == other

    def __getitem__(self, key):
        if key < len(self.__dna_string):
            return self.__dna_string[key]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        if key >= len(self.__dna_string) or key <= -len(self.__dna_string) - 1:
            raise IndexError
        if value not in "ACTG":
            raise ValueError
        self.__dna_string = self.__dna_string[:key] + value + self.__dna_string[key + 1:]

    def __len__(self):
        return len(self.__dna_string)
