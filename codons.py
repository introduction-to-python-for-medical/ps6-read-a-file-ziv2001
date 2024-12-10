

def create_codon_dict(file_path):
    with open(file_path, 'r') as file:
        rows = file.readlines()  

    codon_to_amino = {}

    for row in rows:
        row = row.strip()  # הסרת רווחים מיותרים בתחילת וסוף השורה
        if not row:  
            continue

        split_row = row.split()  

        if len(split_row) >= 2:  
            codon_to_amino[split_row[0]] = split_row[1] 

    return codon_to_amino  
