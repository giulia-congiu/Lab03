import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self, lingua):
        self.dizionario = d.Dictionary.loadDictionary(self, lingua+".txt")
        # self.italiano = d.Dictionary.loadDictionary(self, "Italian.txt")
        # self.spagnolo = d.Dictionary.loadDictionary(self, "Spanish.txt")

    def printDic(self, language):
        pass

    def searchWord(self, words, language):
        parole=words.split()
        # for i in parole:
        pass


