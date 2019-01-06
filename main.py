from huffman import Huffman

h = Huffman()

text = input('Entrez votre texte à décoder.\n')

encoded = h.encode(text)

print (encoded, '\nNombre de bits utilisés : ', h.nBits)
