def complement(base, DNA=True):
    """Find the complement of a base. Change DNA to False for RNA."""
    base_low = base.lower()
    if base_low == 'a':
        comp = 'T' if DNA else 'U'
    elif base_low == 't' or base_low == 'u':
        comp = 'A'
    elif base_low == 'g':
        comp = 'C'
    elif base_low == 'c':
        comp = 'G'
    else:
        comp = 'N'
    return comp

def reverse_complement(sequence, DNA=True):
    """Find the reverse complement of the sequence."""
    rev = ''
    for base in sequence[::-1]:
        print(base, complement(base))
        rev += complement(base)
    return rev

def reverse_complement_no_for(sequence, DNA=True):
    """Find the reverse complement of the sequence without using for loops."""
    rev = sequence[::-1]

    rev = rev.lower()

    rev = rev.replace('a', complement('a', DNA=DNA))

    rev = rev.replace('t', complement('t', DNA=DNA))
    rev = rev.replace('g', complement('g', DNA=DNA))
    rev = rev.replace('c', complement('c', DNA=DNA))
    rev = rev.replace('u', complement('u', DNA=DNA))

    return str(rev)

def longest_common_substring(str1, str2):
    """Find longest common substring."""
    #define shorter and longer strings
    shortStr = str1
    longStr = str2
    if len(str1) > len(str2):
        shortStr = str2
        longStr = str1

    #return entire short string if it is a substring of long string
    if shortStr in longStr:
        return shortStr

    #find all possible substrings of shorter string and store in dictionary
    combo_set = set([])
    d = {j+1:[] for j in range(len(shortStr))}
    for length in d:
        index = 0
        while index + length < len(shortStr) + 1:
            workingSubstring = shortStr[index:index+length]
            if workingSubstring in longStr:
                d[length].append(workingSubstring)
            index += 1
    substringList = sum(list(d.values()), [])
    return substringList[-1]

def equal_parens(parenString):
    """Check if same number of open and closed parentheses."""
    return parenString.count('(') == parenString.count(')')

def dotparen_to_bp(parenString):
    """Converts the dot-parens notation to a tuple of 2-tuples representing the
    base pairs"""
    if not equal_parens(parenString):
        raise RuntimeError('Number of open and closed parentheses different.')
    index = 0
    tupList = []

    while parenString[index] == '(':
        tup = (index, len(parenString) - index - 1)
        tupList.append(tup)
        index += 1

    return tuple(tupList)

def hairpin_requirement(parenString):
    if not equal_parens(parenString):
        raise RuntimeError('Number of open and closed parentheses different.')
    if '...' in parenString:
        return True
    else:
        return False

def rna_ss_validator(seq, sec_struc, wobble=True):
    for tup in dotparen_to_bp(sec_struc):
        if not wobble:
            if seq[tup[0]] != complement(seq[tup[1]], DNA=False):
                return False
        else:
            wobblePair = set([seq[tup[0]], seq[tup[1]]])
            if seq[tup[0]] != complement(seq[tup[1]], DNA=False) and wobblePair != set(['G', 'U']):
                return False
    return True
