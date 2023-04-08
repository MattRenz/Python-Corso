"""Propone moltiplicazioni di numeri tra 1 e 10 verificando se la risposta è corretta, rispondendo 0 deve fermarsi e salutare"""


#print(random.randrange(1,10))

def funzione():
    """Genera in modo casuale DUE numeri da 1 a 10, e controlla il risultato tra essi. Rispondendo 0 finirà il ciclo
    """
    import random
    
    numero1 = random.randrange(1, 10)
    numero2 = random.randrange(1, 10)
    
    print("")
    
    print(f'qunato fa: {numero1} * {numero2}')
    
    risultato = int(input(""))
    
    if numero1 * numero2 == risultato:
        print("Risposta esatta")
    else: print("Risposta sbagliata, riprova")

#risultato coretto  
    risultato_corretto = numero1 * numero2
    
    if risultato_corretto != risultato:
        print(f'Risultato esatto: {risultato_corretto}')

#fine ciclo   
    if risultato == 0: 
        return False
    
    else: return True
    
continua = True
    
while continua: 
    continua = funzione()
   
    if continua == False:
        print("Per oggi hai finito. Ciao e buona giornata")