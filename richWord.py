class RichWord:
    def __init__(self, parola):
        self._parola = parola # this is a string, una parola del testo input
        self._corretta = None #this is a bool, mi serve per dire se la parola è corretta o meno

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self): #metodo usato dalla print
        return self._parola