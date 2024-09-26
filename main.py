from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

print(validateSeq(randDNAStr))