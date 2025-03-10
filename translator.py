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
        diz =  {}
        for line in open(dict,"r"):
            diz.update({line.split(" ")[0] : line.split(" ")[1:]})
        Dictionary.aggiorna_dizionario(diz)

    def handleAdd(self, entry):
        self.entry = entry
        i = self.entry.split(" ")
        tupla = (i[0], i[1:])
        Dictionary.addWord(tupla)

        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass