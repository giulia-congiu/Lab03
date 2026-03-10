import spellchecker

sc = spellchecker.SpellChecker()

def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

while(True):
    sc.printMenu()

    txtIn = input()
    while not txtIn.isdigit() or not (1 <= int(txtIn) <= 4):
        print("ERRORE, INSERISCI UN NUMERO DA 1 A 4!")
        txtIn = input()  # torno all'inizio

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = replaceChars(input().lower())
        sc.handleSentence(txtIn,"italian")
        continue

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(txtIn) == 4:
        break


