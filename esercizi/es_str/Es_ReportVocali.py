"""Stesso procedimento dell'esercizio 3 con l'aggiunta del ciclo"""

def funzione():
    """

    :return: Esegue un ciclo che trova il numero di vocali presenti in una stringa e se è presente la parola python. Se trova la parola basta il processo si ferma
    """
    frase = input("Scrivi una frase a tuo piacimento")

    a = frase.count("a")
    e = frase.count("e")
    i = frase.count("i")
    o = frase.count("o")
    u = frase.count("u")

    if frase.find("python") > -1:
        print("è presente la parola python")
    else:
        print("Non è presente la parola python")

    print("Nella frase sono presenti: ")
    print(f'{a} lettere a')
    print(f'{e} lettere e')
    print(f'{i} lettere i')
    print(f'{o} lettere o')
    print(f'{o} lettere u')

    if frase.find("basta") > -1:
        return False
    else:
        return True

continua = True

while continua:
    continua = funzione()