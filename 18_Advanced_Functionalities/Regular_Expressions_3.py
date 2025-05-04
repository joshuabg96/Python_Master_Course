import re

def search(pattrons, text):
    for patron in pattrons:
        print(re.findall(patron, text))
    print("\n")

text = "haala heeela hiiiila hooooola"

patterns = ["h[ae]la","h[ae]*la","h[io]{3,9}la"]
search(patterns, text)

text = "hala hela hila hola hula"
patterns = ["h[o]la", "h[^o]la"]
search(patterns, text)

text = "hola h0la Hola mola m0la Mla sdjh sdZd"
patterns = ["h[a-z]la", "h[0-9]la", '[A-z]{4}', "[A-z][A-z0-9]{3}"]
search(patterns, text)

text = "Este curso de puthon 3 se publicó en el año 2016"
patterns = [r'\d', r'\d+']
search(patterns, text)