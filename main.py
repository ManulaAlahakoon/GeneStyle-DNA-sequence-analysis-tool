from DNAToolkit import *
from utilities import colored
import random
import streamlit as st

randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
validatedDNAStr = validateSeq(randDNAStr)

st.markdown(f'**Sequence:** {colored(validatedDNAStr)}', unsafe_allow_html=True)

st.write(f'(1) - Sequence Length: {len(validatedDNAStr)}')

nucleotide_frequency = countNucliotideFrequency(validatedDNAStr)

st.markdown(f'(2) - Nucleotide Frequency: {colored(str(nucleotide_frequency))}', unsafe_allow_html=True)

st.markdown(f'(3) - DNA/RNA Transcription: {colored(transcription(validatedDNAStr))}', unsafe_allow_html=True)

st.markdown(f'(4) - DNA String + Reverse Complement:', unsafe_allow_html=True)

st.markdown(f"5' &nbsp;&nbsp;{colored(validatedDNAStr)} &nbsp;&nbsp;3'", unsafe_allow_html=True)

st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;&thinsp;{'&thinsp;'.join(['|&emsp13;' for _ in range(len(validatedDNAStr))])}", unsafe_allow_html=True)

st.markdown(f"3' &nbsp;&nbsp;{colored(reverse_complement(validatedDNAStr))} &nbsp;&nbsp;5'", unsafe_allow_html=True)



# from DNAToolkit import *
# from utilities import colored
# import random
# import streamlit as st

# randDNAStr = ''.join([random.choice(Nucleotides)
#                      for nuc in range(50)])

# validatedDNAStr = validateSeq(randDNAStr)
# print(f'\nSequence: {colored(validatedDNAStr)}')
# st.write(f'\nSequence: {colored(validatedDNAStr)}')
# print(f'\n(1) - Sequence Length: {len(validatedDNAStr)}')
# print(colored(f'\n(2) - Nucletide Frequency: {countNucliotideFrequency(validatedDNAStr)}'))
# print(f'\n(3) - DNA/RNA Transcription: {colored(transcription(validatedDNAStr))}')

# print(f'\n(4) - DNA String + Reverse Complement:')
# print(f'\n5` {colored(validatedDNAStr)} 3`')
# print(f"\n   {''.join(['|' for c in range(len(validatedDNAStr))])}")
# print(f'\n3` {colored(reverse_complement(validatedDNAStr))} 5`')

