"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """
    Convert a DNA seqence to RNA.
    """

    # Convert to uppercase
    seq = seq.upper()

    return seq.replace('T', 'U')
