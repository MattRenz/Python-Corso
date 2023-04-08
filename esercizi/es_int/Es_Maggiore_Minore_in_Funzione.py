"""
Trova se un numero è maggiore o minore e stampalo 
"""
def MaggioreMinore(numero1, numero2): 
    
    if numero1 > numero2:
        print(f'{numero1} maggiore di {numero2}')
    elif numero2 > numero1: 
        print(f'{numero2} maggiore di {numero1}')
    else: 
        print(f'{numero1} e {numero2} uguali')
       
numero1 = int((input(" ")))
numero2 = int((input(" ")))
  
MaggioreMinore(numero1, numero2)