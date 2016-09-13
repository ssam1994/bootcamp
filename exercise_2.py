#lesson_2
import bioinfo_dicts

def store_fasta_as_string(fasta_file_path):
    """Read fasta file and return just the sequence."""
    with open(fasta_file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        if line[0] == '>':
            lines.remove(line)

    joined = ''.join(lines)
    joined = joined.replace('\n', '')

    return(joined)

def gc_blocks(seq, block_size):
    """Find GC content for sequence blocks."""
    num_blocks = len(seq)//block_size
    tups = ()
    for i in range(0, block_size*num_blocks, block_size):
        block = seq[i:i+block_size].lower()
        gCount = block.count('g')
        cCount = block.count('c')
        content =  (gCount + cCount)/block_size
        tups += (content, )

    return tups

def gc_map(seq, block_size, gc_thresh):
    """Returns sequence where every base in a block with GC content
    above threshold is caps blocks below threshold is lowercase"""
    num_blocks = len(seq)//block_size
    returnString = ''
    for i in range(0, block_size*num_blocks, block_size):
        block = seq[i:i+block_size].lower()
        gCount = block.count('g')
        cCount = block.count('c')
        content =  (gCount + cCount)/block_size
        if content >= gc_thresh:
            returnString += block.upper()
        else:
            returnString += block

    return returnString

def salmonella_pathogenicity():
    salmonella_path = """/Users/Sarah/Documents/First-Year/bootcamp/git/bootcamp/data/salmonella_spi1_region.fna"""
    sal_string = store_fasta_as_string(salmonella_path)
    m = gc_map(sal_string, 1000, 0.45)

    with open('salmonella-pathogenicity-map.txt', 'w') as f:
        f.write('>header' + '\n')
        i = 0
        while i < len(m):
            f.write(m[i:i+60] + '\n')
            i += 60
    return m

def longest_orf(dna_seq):
    orf_start = 'atg'
    orf_end = ['tga', 'tag', 'taa']

    start_inds = []

    sub_seq = dna_seq.lower()
    if orf_start not in sub_seq:
        return ''
    while orf_start in sub_seq:
        i = sub_seq.find(orf_start)
        start_index = dna_seq.lower().find(sub_seq[i:])
        start_inds.append(start_index)
        sub_seq = sub_seq[i+1:]

    orfs = []
    dna_seq = dna_seq.lower()

    for start in start_inds:
        for index in range(start, len(dna_seq), 3):
            if any(item in dna_seq[index:index+3] for item in orf_end):
                orfs.append(dna_seq[start:index+3])

    if not orfs:
        print("Did not find any orfs.")
        return None

    return max(orfs).upper()

def salmonella_orfs():
    salmonella_path = """/Users/Sarah/Documents/First-Year/bootcamp/git/bootcamp/salmonella-pathogenicity-map.txt"""
    salmonella_seq = store_fasta_as_string(salmonella_path)
    m = longest_orf(salmonella_seq)
    with open('salmonella-long-orf.fasta', 'w') as f:
        f.write('>header' + '\n')
        i = 0
        while i < len(m):
            f.write(m[i:i+60] + '\n')
            i += 60
    return m

def translate(dna_seq):
    codon_to_aa = bioinfo_dicts.codons
    protein_seq = ''

    for index in range(0, len(dna_seq), 3):
        codon = dna_seq[index:index+3]
        protein_seq += codon_to_aa[codon]

    return protein_seq

def translate_salmonella_orf():
    orf = salmonella_orfs()
    return translate(orf)

def concat_strings(a, b, **kwargs):
    seq = a + b
    for key in kwargs:
        seq += kwargs[key]
    return seq
