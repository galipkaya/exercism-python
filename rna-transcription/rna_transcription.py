rna_complement = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U",
    "": ""
}


def to_rna(dna_strand):
    return "".join([rna_complement.get(dna) for dna in dna_strand])
