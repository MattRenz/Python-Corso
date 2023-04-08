""" 
Esegue la somma di tutti i numeri peresenti in una lista
"""
def sommatore(lista):
    
    molt = 1
    for x in lista:
        if x != 0:
            molt *= x
        
    print(molt)
    
lista = [5, 5, 6]

sommatore(lista)