import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.paroleSbagliate=[]
        self.paroleSbagliate2=[]
        self.paroleSbagliate3=[]
        self.numParoleErrate = None
        self.tempoDiCalcolo = None


    def handleSentence(self, txtIn, language):
        self.paroleSbagliate.clear()
        dizionario= md.MultiDictionary()
        dizionario.printDic(language)
        text= replaceChars(txtIn).lower().split()


        inizio = time.time()
        self.paroleSbagliate.extend(dizionario.searchWord(text))
        fine = time.time()

        self.tempoDiCalcolo = fine - inizio
        self.numParoleErrate=len(self.paroleSbagliate)

        print(f"Parole errate usando Contains: {self.numParoleErrate}")
        print(f"Time elapsed: {self.tempoDiCalcolo:.9f}")
        for parola in self.paroleSbagliate:
            print(parola)

        print("-"*410)

        #lineare
        self.paroleSbagliate2.clear()
        inizio = time.time()
        self.paroleSbagliate2.extend(dizionario.searchWordLinear(text))
        fine = time.time()

        self.tempoDiCalcolo = fine - inizio
        self.numParoleErrate = len(self.paroleSbagliate2)

        print(f"Parole errate usando Ricerca Lineare: {self.numParoleErrate}")
        print(f"Time elapsed: {self.tempoDiCalcolo:.9f}")
        for parola in self.paroleSbagliate2:
            print(parola)

        print("-" * 410)

    #dicotomica
        self.paroleSbagliate3.clear()
        inizio = time.time()
        self.paroleSbagliate3.extend(dizionario.searchWordLinear(text))
        fine = time.time()

        self.tempoDiCalcolo = fine - inizio
        self.numParoleErrate = len(self.paroleSbagliate3)

        print(f"Parole errate usando Ricerca Dicotomica: {self.numParoleErrate}")
        print(f"Time elapsed: {self.tempoDiCalcolo:.9f}")
        for parola in self.paroleSbagliate3:
            print(parola)




    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!?$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text