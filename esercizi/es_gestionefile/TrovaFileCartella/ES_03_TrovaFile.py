""" 
Trova file tramite un pezzo di nome o per estenzione
"""

import Funzioni_TrovaFile as proc

print(" ")
print("inserisci l'estenzione o il nome del file che cerchi per trovare il file")
print(" ")


#input utente 

ModoRIcerca = str(input("Scegli se cercare per nome o per estenzione: ".lower()))
print("")
sDirectory = input("Inserisci cartella: ")
print("")
sRicerca = input("Inserisci ricerca: ")


# richiamo funzione (da file "Procedure_Utili")
miaLista = proc.CercaFilePerEstenione(sDirectory, sRicerca)

miaListaNome = proc.CercaFilePerNome(sDirectory, sRicerca)



# stampa il file trovato tramite l'estenzione 
if ModoRIcerca == "estenzione":
    print("")
    print("Stai cercando per estenzione")
    if len(miaLista) == 0: # se non sono presenti file
        print(" ")
        print("Non è stato trovato nessun file") # indica che non sono presenti file
    else: # se sono pesenti i file (quindi la lungezza della lista è diversa da 0) 
        print(" ")
        print("File trovati: ", len(miaLista)) # ci riporta la lunghezza della lista e quindi quanti file sono presenti
        # e infine li stampa
        for file in miaLista:  # li stampa uno per volta con un ciclo for
            print("")
            print(file)
        
        
# modo ricerca per NOME

if ModoRIcerca == "nome":  
    print("")
    print("Stai ricerdando per nome")
    
    if len(miaListaNome) == 0:
        print("")
        print("Non è stato trovato nessun file")
    else: 
        print("")
        print("FIle trovati: ", len(miaListaNome))
    
        for file in miaListaNome:
            print("")
            print(file)
    