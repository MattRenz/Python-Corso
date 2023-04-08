""" 
Ci dice quanti caratteri ci sono in una stringa
"""
def CaratteriInUnaFrase(frase):
    
    for x in range(97, 123):
        lettera = chr(x)
        
        occorenza = frase.count(lettera)
        
        if occorenza > 0:
            print(f'{occorenza} lettere {lettera}')
            
frase = input("Frase: ")
CaratteriInUnaFrase(frase)