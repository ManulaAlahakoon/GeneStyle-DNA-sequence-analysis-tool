from structures import *

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucliotideFrequency(seq):
    tmpFreqDict = {"A":0,"C":0,"G":0,"T":0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    """DNA -> RNA Transcription"""
    return seq.replace("T","U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string"""
    return ''.join([DNA_ReversComplement[nuc] for nuc in seq])[::-1]
