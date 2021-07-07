from DnaSequence import DnaSequence

if __name__ == '__main__':
    dna1 = DnaSequence("ATTC")
    dna1.insert('G', 2)
    print(dna1)
    dna2 = DnaSequence("AC")
    dna2.assignment("ACTGGACTG")
    print(dna2)
    print(dna2 != dna1)
    dna2.assignment(dna1)
    print(dna1)
    print(dna1 == dna2)
    print(dna1[2])
    print(len(dna1))
    dna1[2] = "T"
    print(dna1)
