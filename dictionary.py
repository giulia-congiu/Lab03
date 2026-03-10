class Dictionary:
    def __init__(self):
        self.dict= {}

    def loadDictionary(self, nomefile):
        with open(nomefile, "r", encoding='utf-8') as file:
            for riga in file:
                parola = riga.strip()
                self.dict[parola]=parola

    def printAll(self):
        pass

    @property #getter!!
    def dict(self):
        return self._dict