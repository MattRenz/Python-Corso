""" 
Scrivi una procedura conta vocali che prende come input una stringa, e da come output un intero che è il numero delle vocali

"""


def conta_vocali(stringa):

    vocali = "aeiouàèéùì"

    stringa = stringa.lower()

    vocaliInStr = 0

    for i in stringa:
 
        if i in vocali:

            vocaliInStr +=1

    return vocaliInStr
        

stringa = input("Stringa: ")

numeroVocali = conta_vocali(stringa)

s = f'Nella parola {stringa} ci sono {numeroVocali} vocali'

print(s)

        
    