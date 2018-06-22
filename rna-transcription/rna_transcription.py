def to_rna(dna_strand):
    word=[]
    for a in dna_strand:
        if a=="C":
            word.append("G")
            return word
        elif a=="G":
            word.append("C")
        elif a=="T":
            word.append("A")
        else:
            word.append("U")
    return word


