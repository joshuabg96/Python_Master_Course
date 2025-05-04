import re

text = "hla hola hoola hooola hooooola"
def search(pattrons, text):
    for patron in pattrons:
        print(re.findall(patron, text))

patron = ["hla", "hola", "hoola"]
search(patron, text)


patron = ["ho*", "ho+"]
search(patron, text)


patron = ["ho*", "ho+", "ho?"]
search(patron, text)

patron = ["ho*", "ho+", "ho?","ho?la"]
search(patron, text)


patron = ["ho{0}la", "ho{1}la", "ho{3}la"]
search(patron, text)

patron = ["ho{0,1}la"]
search(patron, text)
