class Dictionary:
    def __init__(self):
        self.lista=[]

    @property  # getter!!
    def dizionario(self):
        return self.lista

    def loadDictionary(self, file):
        with open(file, "r", encoding='utf-8') as file:
            for riga in file:
                parola = riga.strip()
                self.lista.append(parola)

    def printAll(self):
        pass

