def translate(DNA_seq):
    codontable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
    i=0
    AA_seq=''
    while i<len(DNA_seq):
        AA_seq=AA_seq+codontable[DNA_seq[i:i+3]]
        i=i+3
    return AA_seq

def complementary(seq_input):
    '''
    用于获取互补链
    '''
    seq_output=''
    seq=seq_input[::-1]
    for i in seq:
        if i=="A":
            seq_output=seq_output+"T"
        elif i=="T":
            seq_output=seq_output+"A"
        elif i=="G":
            seq_output=seq_output+"C"
        elif i=="C":
            seq_output=seq_output+"G"
    #print ("hello")
    return (seq_output)


seq="acGCTt"
seq=seq.upper()