"""Stampa quanti caratteri di lettere ci sono in una frase"""

def funzione():
        frase = input("inserisci frase: ") #input di una frase
        
        if frase.find("basta") > 1: 
                return False
        
        print("Nella frase inserita sono presenti: ")
        
        for x in range(97,123): #esegui il ciclo del range tra 97 e 122
                
                car = chr(x) #car = corrispettiva lettera del ciclio di numeri unicode
                
                occorenza = frase.count(car) #la variabile occorenza è UGUALE a frase + trova quanti caratteri della lettera de ciclo ci sono
                
                if occorenza > 0: #se la variabile occorenza è maggiore di 0 stampa:
                        print(f'{occorenza} lettere {car}') # numero di volte che si ripete la lettera + lettera 
                        
        return True

continua = True

while continua: 
        continua = funzione()
        
        