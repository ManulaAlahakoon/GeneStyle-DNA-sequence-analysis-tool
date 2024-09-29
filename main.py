from DNAToolkit import *
import random

randDNAStr = ''.join([random.choice(Nucleotides)
                     for nuc in range(50)])

validatedDNAStr = validateSeq(randDNAStr)
print(f'\nSequence: {validatedDNAStr}')
print(f'\n(1) - Sequence Length: {len(validatedDNAStr)}')
print(f'\n(2) - Nucletide Frequency: {countNucliotideFrequency(validatedDNAStr)}')
print(f'\n(3) - DNA/RNA Transcription: {transcription(validatedDNAStr)}')

print(f'\n(4) - DNA String + Reverse Complement:')
print(f'\n5` {validatedDNAStr} 3`')
print(f"\n   {''.join(['|' for c in range(len(validatedDNAStr))])}")
print(f'\n3` {reverse_complement(validatedDNAStr)} 5`')

