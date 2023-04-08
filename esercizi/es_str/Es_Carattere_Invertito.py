""" 
Inverti la frase
"""
def CarattereInvertito(parola):
    
    x = list(parola)
    
    x.reverse()
    
    print(x)
    
parola = input(" ")

CarattereInvertito(parola)