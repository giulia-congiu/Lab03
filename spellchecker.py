import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.paroleSbagliate=[]
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