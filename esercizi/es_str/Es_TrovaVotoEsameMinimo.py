def TrovaMinimo(listaVotiMario): 

    indiceMinimo = 0
    indiceCorrente = 0

    for i in listaVotiMario:

        if i < listaVotiMario[indiceMinimo]:
            indiceMinimo = indiceCorrente

        indiceCorrente +=1
            

    return indiceMinimo


def EsameMario(listaEsamiMario):
    
    esameMario = listaEsamiMario[TrovaMinimo(listaVotiMario)]

    return esameMario



listaVotiMario =  [27,22,25,30,24,28,21,18]
listaEsamiMario = ["Fisica", "Chimica", "Meccanica", "Mecanica2", "Geometria", "Analisi1", "Analisi2", "Chimica organica"]


MaxVoto= TrovaMinimo(listaVotiMario)

Esame = EsameMario(listaEsamiMario)

s = f'Il voto più basso di Mario è {listaVotiMario[MaxVoto]} ed è in {Esame}'

print(s)

