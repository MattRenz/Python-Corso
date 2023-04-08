def MaxVotoMario(listaVotiMario): 

    indiceMassimo = 0
    indiceCorrente = 0

    for i in listaVotiMario:

        if i > listaVotiMario[indiceMassimo]:
            indiceMassimo = indiceCorrente

        indiceCorrente +=1
            

    return indiceMassimo


def EsameMario(listaEsamiMario):
    
    esameMario = listaEsamiMario[MaxVotoMario(listaVotiMario)]

    return esameMario





listaVotiMario =  [27,22,25,23,24,28,21,18]
listaEsamiMario = ["Fisica", "Chimica", "Meccanica", "Mecanica2", "Geometria", "Analisi1", "Analisi2", "Chimica organica"]


MaxVoto= MaxVotoMario(listaVotiMario)

Esame = EsameMario(listaEsamiMario)

s = f'Il voto più alto di Mario è {listaVotiMario[MaxVoto]} ed è in {Esame}'

print(s)
