def code_for_same_protein(seq1,seq2):
    dna1 = [codons.get(seq1[i: i+3], "") for i in range(0, len(seq1), 3)]
    dna2 = [codons.get(seq2[i: i+3], "") for i in range(0, len(seq2), 3)]
    return dna1 ==dna2