""" 
Trova il maggiore tra tre numeri
"""
def funzione(numero1, numero2, numero3): 
    
    if numero1 > numero2 and numero1 > numero3:
        print(f'{numero1} più grande')
        
    if numero2 > numero1 and numero2 > numero3:
        print(f'{numero2} più grande')
        
    if numero3 > numero1 and numero3 > numero2:
        print(f'{numero3} più grnade')

numero1 = int(input(" "))
numero2 = int(input(" "))
numero3 = int(input(" "))


funzione(numero1, numero2, numero3)