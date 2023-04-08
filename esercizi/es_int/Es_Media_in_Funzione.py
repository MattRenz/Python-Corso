""" 
Trova la media tra una lista di numeri
"""
def Media(lista):
    
    somma = 0
    for x in lista: 
        somma+=x
        
    media = somma / len(lista)
        
    print(f'Media: {media}')
    
lista = [5, 7, 8, 2]

Media(lista)
    
        
    