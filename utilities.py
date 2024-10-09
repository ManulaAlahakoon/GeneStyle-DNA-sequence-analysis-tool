"""def colored(seq):
    bcolors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc] + nuc
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + '\033[0;0m'
"""

# def colored(seq):
#     color_map = {
#         'A': 'lightgreen',
#         'C': 'lightblue',
#         'G': 'lightorange',
#         'T': 'lightred',
#         'U': 'lightred',
#     }

#     tmpStr = ""

#     for nuc in seq:
#         if nuc in color_map:
#             tmpStr += f'<span style="color:{color_map[nuc]}">{nuc}</span>'
#         else:
#             tmpStr += f'<span>{nuc}</span>'

#     return tmpStr


def colored(seq):
    bcolors = {
        'A': '<span style="color: #00FF00; font-size: 20px;">A</span>',  # Bright green
        'C': '<span style="color: #0000FF; font-size: 20px;">C</span>',  # Bright blue
        'G': '<span style="color: #FFFF00; font-size: 20px;">G</span>',  # Bright yellow
        'T': '<span style="color: #FF4500; font-size: 20px;">T</span>',  # Bright orange-red
        'U': '<span style="color: #FF4500; font-size: 20px;">U</span>',  # Bright orange-red
        'reset': '</span>'
    }

    tmpStr = ""

    for nuc in seq:
        if nuc in bcolors:
            tmpStr += bcolors[nuc]
        else:
            tmpStr += bcolors['reset'] + nuc

    return tmpStr + bcolors['reset']
