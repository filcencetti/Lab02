import translator as tr
t = tr.Translator()
while(True):
    t.printMenu()
    t.loadDictionary("dictionary.txt")
    txtIn = input()
    if txtIn.isnumeric() == False:
        raise KeyError("Il valore inserito non è valido!!!")
    if int(txtIn) == 1:
        risposta = input("Ok, quale parola vuoi aggiungere?\n")
        t.handleAdd(risposta)
    elif int(txtIn) == 2:
        pass
    elif int(txtIn) == 3:
        pass
    elif int(txtIn) == 4:
        break