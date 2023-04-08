
""" 
Programma che chieda all'utente quanti numeri vuole sommare, e che poi richiede i numeri e li somma tra loro
Coregge se l'utente sbaglia e non inserisce un numero, ritorna alla richiesta, dopo 3 tentativi il programma si blocca 
"""

import sys

tentativi = 3 # tentativi

tentativiCorrenti = 0 

iNumNUmeri = 0

while tentativiCorrenti < tentativi: # quando l'utene ha raggiunto i 3 tentativi blocca l'esecuzione
    
    try: 
        iNumNUmeri = input("Quanti numeri vuoi sommare? ") 
        iNumNUmeri = int(iNumNUmeri) # eccezione: se non ha inserito degli interi (sappiamo l'errore e gli diciamo cosa fare in caso si socntra con l'errore)
        tentativiCorrenti = 100
    except: # quando la funzione va in errore entriamo dentro except
        
        #StampaErrorMsg(sNumeri) # ciclo for che appena trova una cifra che non è un numero riporti l'errore
        
        print(f'ERRORE: Inserire solo valori numerici, {iNumNUmeri} non è un valore numerico')
        
        tentativiCorrenti += 1
        
        if tentativiCorrenti == tentativi:
            sys.exit(0) # quando usciamo ci dice sei uscito con codice 0 (perché ho inserito 0)
        



tentativi2 = 0

somma = 0

for i in range(0, iNumNUmeri):
    
    while tentativi2 < 3:
        
        try:
            NumeriDaSommare = int(input(f'Inserisci numero:  '))
            
            somma = somma + NumeriDaSommare
            
            tentativi2 = 0
            
            break
        except: 
            print(f'ERRORE: inserire solo valori numerici, {NumeriDaSommare} non è valido')
            tentativi2 += 1
            if tentativi2 == 3:
                sys.exit()
                  
                  
print(f'La somma è {somma}')        
    