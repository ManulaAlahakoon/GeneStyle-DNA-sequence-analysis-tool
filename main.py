from DNAToolkit import *
from utilities import colored
import random
import streamlit as st

colors = {
    'G': '#00FF00',  # Green for G
    'E': '#0000FF',  # Blue for E
    'N': '#FF0000',  # Red for N
    'S': '#FFFF00',  # Yellow for S
    'C': '#00FF00',  # Green for C
    'O': '#0000FF',  # Blue for O
    'P': '#FF0000',  # Red for P
    'E_last': '#FFFF00'  # Yellow for last E
}


st.markdown(f"<h1 style='text-align:center;'>"
            f"<span style='color:{colors['G']}'>G</span>"
            f"<span style='color:{colors['E']}'>e</span>"
            f"<span style='color:{colors['N']}'>n</span>"
            f"<span style='color:{colors['S']}'>e</span>"
            f"<span style='color:{colors['C']}'>S</span>"
            f"<span style='color:{colors['O']}'>c</span>"
            f"<span style='color:{colors['P']}'>o</span>"
            f"<span style='color:{colors['E_last']}'>p</span>"
            f"<span style='color:{colors['G']}'>e</span></h1>", 
            unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center; font-size:14px;'>DNA sequence analysis tool</h3>", unsafe_allow_html=True)
st.markdown('<hr>', unsafe_allow_html=True)


randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
inputDNAStr = st.text_input("Input a DNA Sequence of your own:")

def randomBtn():
    print('Refresh')

# st.button('Random', on_click=randomBtn) 
# st.caption("Textfield should be empty to generate random DNA sequence")

if inputDNAStr == '':
    randDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])
else:
    randDNAStr = inputDNAStr
    
validatedDNAStr = validateSeq(randDNAStr)




if validatedDNAStr:
    st.subheader("Sequence:")
    st.markdown(f'{colored(validatedDNAStr)}', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.subheader("Sequence Length:")
    st.markdown(f'<h3 style="font-size:20px;">{len(validatedDNAStr)}</h3>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    nucleotide_frequency = countNucliotideFrequency(validatedDNAStr)
    
    st.subheader("Nucleotide Frequency:")
    st.markdown(f'<h3 style="font-size:20px;">{colored(str(nucleotide_frequency))}</h3>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.subheader("DNA/RNA Transcription:")
    st.markdown(f'<h3 style="font-size:20px;">{colored(transcription(validatedDNAStr))}</h3>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    st.subheader("DNA String + Reverse Complement:")
    
    st.markdown(f"5' &nbsp;&nbsp;{colored(validatedDNAStr)} &nbsp;&nbsp;3'", unsafe_allow_html=True)
    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;&thinsp;{'&thinsp;'.join(['|&emsp13;' for _ in range(len(validatedDNAStr))])}", unsafe_allow_html=True)
    st.markdown(f"3' &nbsp;&nbsp;{colored(reverse_complement(validatedDNAStr))} &nbsp;&nbsp;5'", unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

elif validatedDNAStr == False:
    st.html("<h3 style='color:red;'>DNA String is not acceptable.</h3>")


st.button('Random', on_click=randomBtn, key=2) 
st.caption("Textfield should be empty to generate random DNA sequence")

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

