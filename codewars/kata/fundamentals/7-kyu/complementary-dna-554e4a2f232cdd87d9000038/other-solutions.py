# -------------------------------------------------------------------------------------------------

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

# -------------------------------------------------------------------------------------------------

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

# -------------------------------------------------------------------------------------------------

def DNA_strand(dna):
    reference = { "A":"T",
                  "T":"A",
                  "C":"G",
                  "G":"C"
                  }
    return "".join([reference[x] for x in dna])

# -------------------------------------------------------------------------------------------------

import string

def DNA_strand(dna):
    return dna.translate(string.maketrans('ATCG', 'TAGC'))

# -------------------------------------------------------------------------------------------------

def DNA_strand(dna):
    # code here
    dnaComplement=""
    for string in dna:
        if string=="A":
            dnaComplement+="T"
        elif string =="T":
            dnaComplement+="A"
        elif string =="G":
            dnaComplement+="C"
        elif string == "C":
            dnaComplement+="G"
    return dnaComplement

# -------------------------------------------------------------------------------------------------
