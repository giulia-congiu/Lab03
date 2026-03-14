import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dizionario = d.Dictionary() # ← oggetto di tipo Dictionary


    def printDic(self, language):
        file = "resources/" + language+".txt"
        self.dizionario.loadDictionary(file)


    def searchWord(self, words):
        paroleErrate=[]
        for i in words:
            parola=rw.RichWord(i)
            if i not in self.dizionario.lista:
                parola.corretta= False
                paroleErrate.append(parola)
            else :
                parola.corretta= True
        return paroleErrate

    def searchWordLinear(self, words):
        paroleErrate = []
        for i in words:
            parola = rw.RichWord(i)
            for j in self.dizionario.lista:
                if i==j:
                    parola.corretta = True
                    break
            if not parola.corretta:
                paroleErrate.append(parola)
        return paroleErrate

    def searchWordDichotomic(self, words):
        paroleErrate = []
        for i in words:
            parola = rw.RichWord(i)
            inizio = 0
            fine = len(self.dizionario.lista) - 1 #è l'indice dell'ultimo elemento e tengo conto che gli indici partono da 0

            while inizio <= fine:
                medio = (inizio + fine) // 2
                if self.dizionario.lista[medio] == i:
                    parola.corretta = True
                    break
                elif self.dizionario.lista[medio] < i: #uso < xchè controlla le stringhe in ordine alfabetico
                    inizio =  medio +1
                else:
                    fine =  medio -1
            if not parola.corretta:
                paroleErrate.append(parola)
        return paroleErrate
