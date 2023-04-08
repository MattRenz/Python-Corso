import random

codici = list(range(1, 54)) #alfabeto da 1 a 54 per inserie anche le lettere maiuscole

random.shuffle(codici) # riorganizza la lista in modo casuale

lettere = []

for n in range(65, 91):  # range di numeri del codice asci
    
    lettera = chr(n) # dal range alle lettere 
    lettere.append(lettera) # aggiungi le lettere alla lista vuota
    lettere.append(lettera.lower()) # oltre quelle che hai aggiunto aggiungi le lettere minusocle
    

diz = {} #creazione dizionario vuoto

for idx, c in enumerate(lettere):  
    diz[c] = codici[idx]
    

print(diz)   # dizionario 
print(diz.get("B")) # numero corrispondente a B

diz[" "] = " "


def funzione():
    """ 
    1) Creare una frase dell'utente 
    
    2) Inserire ogni singolo carattere all'interno di una lista
    
    3) confrontare le lettere della frase, con le lettere del dizionario, e tirarsi fuori i numeri corrispondenti alla lettera
    
    4) inserire i numeri all'interno di una lista

    5) Stamparsi la lista
    """
    
    print("Scrivi una frase".center(80, "_"))
    print("")
    
    frase = input(" ")

    cript = ""
    
    for lettere in frase: 
        cript += str(diz[lettere]) + " "


    print(cript)    
        
    '''
    Il problema è che non riesco a tirarmi fuori le lettere corrispondenti della mia frase con i numeri del dizionario
    '''
    
funzione()
    
  





