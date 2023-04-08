"""Programma che chiede un numero e stampa  se è pari o dispari"""

def pari_Dispari():
    """
    
    :return: riconosce se un numro è pari o dispari 
    """

    par1 = input('Numero')
    
    if int(par1) % 2 == 0:
        print('è pari')
    else:
        print('è dispari')

pari_Dispari()
