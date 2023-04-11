import os

def CartellaBase():
    
    return os.getenv('USERPROFILE') + "/Programma_Segreteria"

percorsoCartellaBase = CartellaBase()
    
def CreazioneCartelle():
    
    percorsoCartellaBase = os.getenv('USERPROFILE') + "/Programma_Segreteria"
    if os.path.exists(percorsoCartellaBase) == False:
        os.mkdir(percorsoCartellaBase)
    
    
    percorsoDocenti = percorsoCartellaBase + "/DB_Docenti"
    if os.path.exists(percorsoDocenti) == False:
        os.mkdir(percorsoDocenti)

    percorsoStudenti = percorsoCartellaBase + "/DB_Studenti"
    if os.path.exists(percorsoStudenti) == False:
        os.mkdir(percorsoStudenti)
        

def GetPercorsoDocenti():
    
    return percorsoCartellaBase + "/DB_Docenti"

def GetPercorsoStudenti():
    
    return percorsoCartellaBase + "/DB_Studenti"

