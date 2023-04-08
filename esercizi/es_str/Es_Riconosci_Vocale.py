"""
Riconosce se un carattere che gli passiamo è una vocale o no  
"""
def funzione(carattere): 
    vocali = "aeioun"
    if carattere in vocali:
        print("E' una vocale")
    else:
        print("Non è una vocale")
        
funzione("a")