class Dictionary:
    def __init__(self,p_aliena,p_ita):
        self.p_ita = p_ita
        self.p_aliena = p_aliena


    def addWord(self):
        dizionario.append(self)


    def translate(self):
        for i in dizionario:
            if self == i.p_aliena:
                print(i.p_ita)

    def translateWordWildCard(self,parola):
        self.parola = parola
        for i in parola.split():
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


    def trad_multiple(self,trad2,trad3):
        self.trad2 = trad2
        self.trad3 = trad3
        dizionario.append(Dictionary(self.p_aliena,[self.p_ita,trad2,trad3]))
        print(f"La parola aliena {self.p_aliena} può avere le seguenti traduzione: {self.p_ita}, {trad2} e {trad3}")

file = open('dictionary.txt','r')
dizionario = []
for line in file.readlines():
    dizionario.append(Dictionary(line.split(" ")[0],line.split(" ")[1]))

import string
alfabeto = []
for i in string.ascii_lowercase:
    alfabeto.append(i)

print("------------------------------\n"
      "   Traslator Alien-Italian\n"
      "------------------------------\n"
      "1. Aggiungi nuova parola\n"
      "2. Cerca una traduzione\n"
      "3. Cerca con wildcard\n"
      "4. Stampa tutto il dizionario\n"
      "5. Exit\n"
      "6. Traduzione multipla\n"
      "-----------------------------")
inp = input()
if inp.isnumeric() == False or int(inp) > 6:
    raise ValueError("Non ha inserito un numero valido")
if inp == "1":
    word = input("Ok, quale parola devo aggiungere?\n")
    if word.isalpha() == False:
        raise KeyError("Devono essere presenti solo lettere alfabetiche!!!")
    else:
        Dictionary(word.split(" ")[0].lower(), word.split(" ")[1].lower()).addWord()
    print("Aggiunta!")


elif inp == "2":
    word = input("Ok, quale parola devo tradurre?\n")
    if word.isalpha() == False:
        raise KeyError("Devono essere presenti solo lettere alfabetiche!!!")
    Dictionary.translate(word)

elif inp == "3":
    Dictionary.translateWordWildCard("a?a")

elif inp == "4":
    for i in dizionario:
        print(i.p_aliena,i.p_ita)


elif inp == "5":
    print("Exit!")

elif inp == "6":
    word = input("Inserisci le opzioni multiple:\n")
    trad_multiple = word.split(" ")
    Dictionary(trad_multiple[0],trad_multiple[1]).trad_multiple(trad_multiple[2],trad_multiple[3])

