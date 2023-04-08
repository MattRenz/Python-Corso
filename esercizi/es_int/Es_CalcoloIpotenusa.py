#Procedure 

import math

def CalcolaIpotenusa(iLenCateto1, iLenCateto2):
    
    iCalcolo = (iLenCateto1 * iLenCateto1) + (iLenCateto2 * iLenCateto2)

    iIpotenusa = math.sqrt(iCalcolo)
    
    return iIpotenusa
    
  
ipotenusa = CalcolaIpotenusa(32, 40)
print(ipotenusa)
