class Dictionary:
    def __init__(self, dict=[]):
        self._lista= dict

    @property  # getter!!
    def lista(self):
        return self._lista

    def loadDictionary(self, file):
        with open(file, "r", encoding='utf-8') as file:
            for riga in file:
                parola = riga.strip()
                self._lista.append(parola)

    def printAll(self):
        for value in self._lista:
            print(f" {value}")

