from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

validatedDNAStr = validateSeq(randDNAStr)
print(f'\nSequence: {validatedDNAStr}')
print(f'\n1 - Sequence Length: {len(validatedDNAStr)}')
print(f'\n2 - Nucletide Frequency: {countNucliotideFrequency(validatedDNAStr)}')
print(f'\n3 - DNA/RNA Transcription: {transcription(validatedDNAStr)}')

