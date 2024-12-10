def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()
    codon_to_amino = {}
    for row in rows:
        split_row = row.strip().split('\t')
    codon_to_amino[split_row[0]]=split_row[2]
    return codon_to_amino


