def to_rna(dna_strand):
    dico = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna = []
    for i in dna_strand:
        rna.append(dico[i])
    return "".join(rna)

if __name__ == '__main__':
    print(to_rna("GCTA"))