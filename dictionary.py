class Dictionary:
    def __init__(self):
        pass

    def addWord(self):

    def translate(self):
        pass

    def translateWordWildCard(self):
        for i in parola.split():  # controllo sulle lettere della parola per trovare il "?"
            val = True
            while i != "?" and val == True:
                for lettera in alfabeto:
                    parola_agg = self.replace("?", lettera)
                    for traduzione in dizionario:
                        if parola_agg == traduzione.p_aliena:
                            print(traduzione.p_ita)
                            val = False
                            break
                        break
                    break
        pass