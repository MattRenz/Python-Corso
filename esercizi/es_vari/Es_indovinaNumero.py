"""
- Un gioco che conta di dover indovinare un umero casuale tra un minimo ed un massimo che possiamo configurare (poniamo tra 1 e 100) 
- Il programma deve continuare a chiede una risposta finché non abbiamo indovinato 
- ogni volta deve dirci se il nostro numero è più grande o più piccolo 
- Una volta indovinato finisce e ci fa i complimenti

"""

def funzione():
    import random
    
    numero = random.randrange(0, 100)
    
    fine_ciclo = 0 
    
    print("Inserisci un numero da 1 a 100")
    
    while fine_ciclo == 0:
        
        risultato = int(input("Numero da 1 a 100: "))
        
        if risultato == numero:
            print("Hai vinto compliimenti")
            fine_ciclo =1
            
            
        elif risultato < numero:
            print("E' più alto")
        else: 
            print("E' più basso")
funzione()
        