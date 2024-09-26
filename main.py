from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

validatedDNA = validateSeq(randDNAStr)
print(countNucliotideFrequency(validatedDNA))