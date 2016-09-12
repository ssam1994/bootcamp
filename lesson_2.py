#lesson_2
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
