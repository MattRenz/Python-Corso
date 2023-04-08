def SommaNumeri(numeriDaSommare):

    numeriDaSommare = int(numeriDaSommare)
      
    numeri = 0

    numeriSum = []
 
    print(f'\nInserisci i tuoi {numeriDaSommare} numeri')

    while numeri < numeriDaSommare:

        numero = int(input("\nNumero: "))
        numeriSum.append(numero)
        numeri+=1

    somma = sum(numeriSum)

    s = f'\nLa somma dei tuoi {numeriDaSommare} numeri è: {somma}'

    return s

tentativi = 0

while tentativi < 3:
    try:
        numeriDaSommare = int(input("\nNumeri da sommare: "))
        sommaNumeri = SommaNumeri(numeriDaSommare)
        print(sommaNumeri)
        break
    except: 
        print("\n ERROE: Inserire solo valori numerici")
        tentativi+=1
    