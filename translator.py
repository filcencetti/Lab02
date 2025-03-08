from dictionary import Dictionary
class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        print("-------------------------------")
        print("Traduttore Alieno-Italiano")
        print("-------------------------------")
        print(" 1. Aggiungi nuova parola")
        print(" 2. Cerca traduzione")
        print(" 3. Cerca con wildcard")
        print(" 4. Stampa tutto il dizionario")
        print(" 5. Exit")
        pass

    def loadDictionary(self, dict):
        dizionario_1 = {}
        for line in open(dict,"r"):
            dizionario_1[line.split(" ")[0]] = line.split(" ")[1:]
        return dizionario_1

    def handleAdd(self, entry):
        self.entry = entry
        dizionario_2 = {}
        i = self.entry.split(" ")
        dizionario_2[i[0]] = i[1:]
        Dictionary.addWord(dizionario_2)
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass