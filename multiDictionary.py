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



