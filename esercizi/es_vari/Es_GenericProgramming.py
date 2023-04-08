def MaxVotoMario(listaVotiMario): 

    indiceMassimo = 0
    indiceCorrente = 0

    for i in listaVotiMario:

        if i > listaVotiMario[indiceMassimo]:
            indiceMassimo = indiceCorrente

        indiceCorrente +=1
            

    return indiceMassimo


def TrovaMaxVoto(dizionarioVotiMario):


    massimo = list(dizionarioVotiMario.values())[0]
    chiaveMax = ""


    for key, value in dizionarioVotiMario.items():

            if value > massimo:

                chiaveMax = key
                massimo = value

    return chiaveMax
    


def TrovaMassimo(lista_diz):
     
    if type(lista_diz) == list:
         
        return MaxVotoMario(lista_diz)

    elif type(lista_diz) == dict:
         
        return TrovaMaxVoto(lista_diz)


listaVotiMario =  [27,22,25,23,24,28,21,18]
listaEsamiMario = ["Fisica", "Chimica", "Meccanica", "Mecanica2", "Geometria", "Analisi1", "Analisi2", "Chimica organica"]


dizionarioVotiMario = {

    "Fisica":27,
    "Chimica":22,
    "Meccanica1":25,
    "Meccanica2":30,
    "Geometria":24,
    "Analisi1":28,
    "Analisi2":21,
    "Chimica organica":18,
}


listaMax = TrovaMassimo(listaVotiMario)

sLista = f'Il voto massimo è {listaVotiMario[listaMax]} in {listaEsamiMario[listaMax]}'

dictMAx = TrovaMassimo(dizionarioVotiMario)

sDict = f'Il voto massimo è {dizionarioVotiMario[dictMAx]} in {dictMAx}'


print(sLista)

print(f'\n {sDict}')