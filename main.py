import spellchecker

sc = spellchecker.SpellChecker()


while(True):
    sc.printMenu()

    txtIn = input()
    while not txtIn.isdigit() or not (1 <= int(txtIn) <= 4):
        print("ERRORE, INSERISCI UN NUMERO DA 1 A 4!")
        txtIn = input()  # torno all'inizio

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"Italian")
        continue
        # Il continue serve per tornare all'inizio del while dopo
        # aver gestito un'opzione, così il menu viene ristampato e l'utente
        # può fare un'altra scelta.

    if int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"English")
        continue

    if int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input().lower()
        sc.handleSentence(txtIn,"Spanish")
        continue

    if int(txtIn) == 4:
        break


