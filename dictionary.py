class Dictionary:
    def __init__(self):
        self.lista_dizionario = {}
        pass

    def aggiorna_dizionario(self,dizio):
        self.lista_dizionario = dizio
        pass

    def addWord(self,tupla):
        è_presente = False
        for i in self.lista_dizionario.keys():
            if i == tupla[0]:
                è_presente = True
                self.lista_dizionario[i] = self.lista_dizionario[i].append(tupla[1:])
                break

        if è_presente == False:
            self.lista_dizionario.update({tupla[0]:tupla[1:]})
        pass

    def translate(self):
        pass

    def translateWordWildCard(self):
        """for i in parola.split():  # controllo sulle lettere della parola per trovare il "?"
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
        """
        pass