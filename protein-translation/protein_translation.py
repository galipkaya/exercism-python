def proteins(strand):
    codon_parts = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    protein_dict = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
    }

    result = []
    for codon in codon_parts:
        protein = protein_dict.get(codon)
        if protein is None:
            return result
        result.append(protein)

    return result
