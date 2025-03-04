class Dictionary:
    def __init__(self,p_aliena,p_ita):
        self.p_ita = p_ita
        self.p_aliena = p_aliena


    def addWord(self):
        dizionario.append(self)


    def translate(self):
        pass

    def translateWordWildCard(self):
        pass

file = open('dictionary.txt','r')
dizionario = []
for line in file.readlines():
    dizionario.append(Dictionary(line.split(" ")[0],line.split(" ")[1]))

print("------------------------------\n"
      "   Traslator Alien-Italian\n"
      "------------------------------\n"
      "1. Aggiungi nuova parola\n"
      "2. Cerca una traduzione\n"
      "3. Cerca con wildcard\n"
      "4. Stampa tutto il dizionario\n"
      "5. Exit\n"
      "-----------------------------\n")
inp = input()
if inp == "1":
    word = input("Ok, quale parola devo aggiungere?\n")
    Dictionary(word.split(" ")[0], word.split(" ")[1]).addWord()
    print("Aggiunta!")

if inp == "2":

if inp == "3":

if inp == "4":

if inp == "5":
    print("Exit!")