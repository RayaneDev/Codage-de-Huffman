class Node :

    def __init__(self, value, letter, left = None, right = None) :

        if left is not None and right is not None :
            left.parent = self
            right.parent = self

            self.left = left
            self.right = right

        self.value = value if value is not None else left.value + right.value
        self.letter = letter

class Huffman :

    def __init__ (self) :
        self.letters = []   # Lettres du texte décodé
        self.occurrences = [] # Fréquence des lettres du texte décodé
        self.occ = {} # Occurrence de chaque lettre

        self.nodes = [] # Noeuds de l'arbre binaire
        self.root = None # Noeud racine
        self.height = 0 # Hauteur maximale de l'arbre binaire
        self.encoded = "" # Bits du texte
        self.decoded = "" # Texte décodé
        self.nBits = 0 # Nombre de bits de l'encodage

        self.bin = [] # Succession des bits classés

        self.table = {} # Table des bits pour chaque lettre

    def encode (self, text) :

        for i in range (0, len(text)) :
            if text[i] not in self.letters :
                self.letters.append(text[i])
                self.occurrences.append(1);
            else :
                self.occurrences[self.letters.index(text[i])] += 1




        for i in range (0, len(self.letters)) :
            self.occ[self.letters[i]] = self.occurrences[i]


        arr = sorted(self.occ.items(), key=lambda kv: kv[1])

        for i in range (0, len(arr)) :
            self.nodes.append(Node(arr[i][1], arr[i][0]))

        i = 0

        while i < len(self.nodes) - 1 :
            self.nodes.append(Node(None, None, self.nodes[i], self.nodes[i+1]))
            i += 2

        self.root = self.nodes[-1]

        for i in range (0, len(arr)) :
            for j in range (0, len(self.nodes)) :
                if arr[i][0] == self.nodes[j].letter :
                    pointer = self.nodes[i]

                    encode_letter = ""

                    if pointer == self.root :
                        encode_letter = "0"
                        self.table[arr[i][0]] = encode_letter
                        break
                    else :
                        n = 0
                        while pointer != self.root :
                            n += 1
                            if pointer.parent.left == pointer :
                                encode_letter += "0"
                            elif pointer.parent.right == pointer :
                                encode_letter += "1"

                            pointer = pointer.parent

                        if n > self.height :
                            self.height = n

                    self.table[arr[i][0]] = encode_letter[::-1]

        self.encoded = ""
        for i in range (0, len(text)) :
            self.encoded += self.table[text[i]]

        self.nBits = len(self.encoded)
        return self.encoded

    def decode (self, seq, table = None) :

        if table is not None and len(self.table) == 0 :
            self.table = table

        i = 0
        while i < len(seq) :
            if seq[:i+1] in self.table.values() :
                self.bin.append(seq[:i+1])
                seq = seq[i+1:]
                i = 0
            i += 1


        for i in range (0, len(self.bin)) :
            for letter, code in self.table.items():
                if code == self.bin[i]:
                    self.decoded += letter

        return self.decoded

h = Huffman()

text = input('Entrez votre texte à décoder.\n')

encoded = h.encode(text)

print (encoded, '\nNombre de bits utilisés : ', h.nBits)
