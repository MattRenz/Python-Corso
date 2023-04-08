"""  
Chiede all'utetne un percorso

Se il percorso esiste ? E' una cartella ? 

Quanti file ci sono ? 

Quanti file ci sono per tipo ? (es 34 pdf)


    
"""


import os

def ContaFile(pathRicerca):

    nmFIle = 0

    listaFile = os.listdir(pathRicerca)

    for file in listaFile:

        pathFile = pathRicerca + "/" + file

        if os.path.isfile(pathFile):

            nmFIle +=1

    s = f'\n Numero file {nmFIle}'

    if nmFIle == 0:

        s = "\n Non sono presenti file dentro questo Path"

    return s


def ListaEstenzioni(pathRicerca):


    listaFile = os.listdir(pathRicerca) #[file.1.pdf, file2.txt, file3.pdf]

    estenzioni = [] # [pdf, txt, pdf]

    for file in listaFile:

        if len(file.split(".")) == 2:

            estenzione = file.split(".")[1] # 1
            estenzioni.append(estenzione)

        if len(file.split(".")) == 3:
        
            estenzione = file.split(".")[2] # 2
            estenzioni.append(estenzione)
        
        if len(file.split(".")) == 4:
        
            estenzione = file.split(".")[3] # 3 
            estenzioni.append(estenzione)

    return estenzioni


def TrovaFilePDF(pathRicerca, estenzione):

    # ['png', 'jpg', 'pdf', 'pdf', 'txt', 'png']

    estenzione = list(set(estenzione))

    # ['png', 'jpg', 'pdf', 'txt', 'png']

    listaFile = os.listdir(pathRicerca)

    tipiFileS = []

    
    for file in estenzione:  # ["pdf"]

        file = file.lower()

        nomeFile = file

        nmTipoFile = 0

        for allFile in listaFile: # [file1.pdf, file2.pdf, file3.txt]

            if allFile.endswith(file):

                nmTipoFile +=1
        
        s = f'File {nomeFile}: {nmTipoFile}'

        tipiFileS.append(s)

    return tipiFileS


# MAIN

print("\n Programma di ricerca file")

pathRicerca = input("\n Path: ")


if os.path.isdir(pathRicerca) == False:

    if os.path.exists(pathRicerca) == True:

        print("Stai cercando un file")

if os.path.isdir(pathRicerca) == True:

    risp = ContaFile(pathRicerca)
    print(risp)

    estenzioni = ListaEstenzioni(pathRicerca)
    RispAllFIle = TrovaFilePDF(pathRicerca, estenzioni)

    for tipoFile in RispAllFIle:

        print(f'\n {tipoFile}')

