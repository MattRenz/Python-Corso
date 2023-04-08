frase = input("Scrivi una frase: ")

fraseInLista = list(frase) #singoli caratteri della lista
    
fraseInLista.reverse()
    
fra = "_".join(fraseInLista)
    
print(fra)
