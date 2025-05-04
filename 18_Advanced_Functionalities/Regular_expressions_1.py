import re

text = "En esta cadena se encuentra una plabra mágica"

re.search('mágica', text)

re.search('hola',text)

word = 'hola'

found = re.search(word, text)

if found is not None:
    print("Word found")
else:
    print("Word not found")


found.start()       # poscition where the word is found
found.end()         # poscition where the word end
found.span()        # tupple of start and end
found.string()      # complete word where it found the special word


text = "Hola mundo"
re.match("Hola",text)        # If the text start with Hola

text = "Vamos a dividir esta cadena"
re.split(' ', text)

text = "Hola amigo"
re.sub("amigo","amiga", text)

text = "hola adios hola hoa"
re.findall('hola',text)

