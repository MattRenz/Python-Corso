
""" 
Calcolatrice che dati 2 numeri ed un operatore calcoli il risultato
Controllo errori:
Controllo se ci sono solo numeri e non caratteri nell'input
Controllo se l'operatore inserito è valido
Dopo 3 errori la calcolatrice si ferma
"""

import sys

def VerificaNUmero(sStringaDaVerificare):
    for car in sStringaDaVerificare:
        
        if(car < "0" or car >"9") and (car != "."): #controlla se sono tutti caratteri
            return 1 
    return 0

print(" ")
print("Calcolatirce".center(80, "_"))
print(" ")
print("Operatori validi: + - * / **".center(40))
print(" ")

def calcolatrice():
    
    numTentativi = 0
                                                                                
    while(numTentativi < 3): 
        numero1 = input("inserisci un numero: ")
        numero2 = input("inserisci un numero: ")
        operatore = input("Operatore: ")
        operatori = "+-*/**"
        if (VerificaNUmero(numero1) == 0 and VerificaNUmero(numero2) == 0):
            numero1 = float(numero1)
            numero2 = float(numero2)
            
            if operatore == "+":
                risultato = numero1 + numero2
                print(f'Il risultato di {numero1} + {numero2} =  {risultato}')
            elif operatore == "-": 
                risultato = numero1 - numero2
                print(f'Il risultato di {numero1} - {numero2} = {risultato}')
            elif operatore == "*":
                risultato = numero1 * numero2
                print(f'Il risultato di {numero1} * {numero2} = {risultato}')
            elif operatore == "/": 
                risultato = numero1 / numero2
                risultato = round(risultato, 2)
                print(f'Il risultato di {numero1} / {numero2} = {risultato}')
            elif operatore == "**":
                risultato = numero1 ** numero2
                print(f'Il risultato di {numero1} ** {numero2} = {risultato}')
                
            if operatore not in operatori:
                print("ERRORE:  Scegli un operatore valido e riporva")
                numTentativi += 1
                return True
            sys.exit()
        else: 
            numTentativi += 1
            print(f'ERRORE: Inserire solo caratteri numerici')
        
        sys.exit()
            

continua = True
while continua:
    continua = calcolatrice()