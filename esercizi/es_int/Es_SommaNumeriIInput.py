def Somma5Numeri():

    print("Programma che fa la somma dei numeri")

    numeri = 0

    numeriUtetne = []

    while numeri < 5:

        numero = int(input("Inserisci un numero: "))
        numeriUtetne.append(numero)
        numeri +=1


    sommaNumeri = sum(numeriUtetne)
    return f'La somma dei tuoi 5 numeri è: {sommaNumeri}'

risultato = Somma5Numeri()
print(risultato)