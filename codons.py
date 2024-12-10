def create_codon_dict(file_path):
    with open(file_path, 'r') as file:
        rows = file.readlines()
    codon_dict = {}
    for row in rows:
        row = row.strip()
        cells = row.split('\t')
        if len(cells) >= 4:
            codon = cells[0]  
            amino_acid = cells[2]  
            codon_dict[codon] = amino_acid

    return codon_dict

