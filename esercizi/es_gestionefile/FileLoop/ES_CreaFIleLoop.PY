"""  
Definire un path
ciclo infito
chiediamo all'utente un nome file, il contenuto, creiamo il file con dentro la frase nel path

"""

def CreazioneFileLoop(nomeFile, contenutoFile, estenzione):

    print("\n Inserie un path dove si preferisce salvare i file creati")
    path = input("\n Path: ")
    
    pathFile = path + "/" + nomeFile + "." + estenzione

    with open(pathFile, "w") as file:

        file.write(contenutoFile)


# main 

while(1):

    nomeFile = input("Nome file: ").lower()

    estenzioneFile = input("Estenzione file: ").lower()

    contenutoFile = input("Contenuto file: ")


    CreazioneFileLoop(nomeFile, contenutoFile, estenzioneFile)
    
















