"""" 
    Realizzare un gioco dove il computer genera una sequenza di 4 cifre che dobbiamo indovinare, a ogni tentativo 
    ci verrà detto quante cifre al posto giusto e quante sbagliate ci sono nella nostra risposta...?
"""

import random

sequenza = [1,2,3,4]
sequenzaDaIndovinare = []
        
while len(sequenza) > 0:
    seleziona = random.randint(0, len(sequenza) -1) 
    numero = sequenza.pop(seleziona)
    sequenzaDaIndovinare.append(numero)


def funzione():
        
    """Gioco che dati 4 sequenze di numeri in ordine chiede all'utente di indovinare la seuqenza in ordine
    """
    
    
    #print(sequenzaDaIndovinare)
    print("")
    print("Indovina la sequenza dei numeri da 1 a 4".center(80, "_"))
    print("")
      
    #test
    
    print
        
    numero1 = int(input(""))
    numero2 = int(input(""))
    numero3 = int(input(""))
    numero4 = int(input(""))
 
 
    if numero1 == sequenzaDaIndovinare[0] and numero2 == sequenzaDaIndovinare[1] and numero3 == sequenzaDaIndovinare[2] and numero4 == sequenzaDaIndovinare[3]:
        print("")
        print("!COMPLIMENTI!".center(50, "_"))
        print("Hai indovinato tutti i numeri nella posizione giusta")
        print("")
        return False
       
    if  numero1 != sequenzaDaIndovinare[0] and numero2 != sequenzaDaIndovinare[1] and numero3 != sequenzaDaIndovinare[2] and numero4 != sequenzaDaIndovinare[3]:
        print("")
        print("Non hai indovinato nessun numero".center(50, "_"))
        print("")
        return True
    
     
    print("Hai indovinato solo: ".center(40, "_"))
    if numero1 == sequenzaDaIndovinare[0]:
        print(f'il numero {numero1} nella posizione gisuta')
        print("")
    if numero2 == sequenzaDaIndovinare[1]:
        print(f'il numero {numero2} nella posizione giusta')
        print("")
    if numero3 == sequenzaDaIndovinare[2]:
        print(f'il numero {numero3} nella posizione giusta')
        print("")
    if numero4 == sequenzaDaIndovinare[3]:
        print(f'il numero {numero4} nella posizione giusta')
        print("")
    
    return True


continua = True
while continua:
    continua = funzione()