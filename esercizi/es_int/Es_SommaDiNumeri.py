
def sommaTreCoppie(): 
    
    a = input("Valore di a: ")
    b = input("Valore di b: ")
    
    somma = int(a) + int(b)
    
    a1 = input("Valore di a1: ")
    b1 = input("Valore di b1: ")

    somma1 = int(a1) + int(b1)
    
    a2 = input("Valore di a2: ")
    b2 = input("Valore di b2: ")

    somma2 = int(a2) + int(b2)
    
    sommaTotale = somma + somma1 + somma2
    
    print(f'La somma è: {sommaTotale}')
    
sommaTreCoppie()