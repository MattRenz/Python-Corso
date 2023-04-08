"""
Trova il numero più grande della lista 
"""
def funzione(lista):
    
    max = 0 
    
    for x in lista:
        if x > max:
            max = x
            
    print(f'Il più grande è {max}')
    
    
lista = [5, 7, 20, 200]

funzione(lista)