""" 
Scrivere una procedura che prende in input una lista di interi e da come output l'indice del massimo
"""

def TrovaMassimo(lista): 


    indiceMassimo = 0
    indiceCorrente = 0

    for i in lista:

        if i > lista[indiceMassimo]:
            indiceMassimo = indiceCorrente

        indiceCorrente +=1
            

    return indiceMassimo



lista = [12, 38, 43, 55, 20, 32, 68, 43]

TrovaMax = TrovaMassimo(lista)

print(f'Lindice massimo è {TrovaMax}. Che vale {lista[TrovaMax]}')

