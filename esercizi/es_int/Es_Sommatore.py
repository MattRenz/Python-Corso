""" 
Esegue la somma di tutti i numeri peresenti in una lista
"""
def sommatore(lista):
    
    somma = 0 
    for x in lista:
        somma+=x
        
    print(somma)
    
lista = [3, 5, 2]

sommatore(lista)