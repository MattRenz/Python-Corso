import os

def CartellaBase():
    
    return os.getenv('USERPROFILE') + "/Programma_Concessionario"

percorsoCartellaBase = CartellaBase()
    
def CreazioneCartelle():
    
    percorsoCartellaBase = os.getenv('USERPROFILE') + "/Programma_Concessionario"
    if os.path.exists(percorsoCartellaBase) == False:
        os.mkdir(percorsoCartellaBase)
    
    
    percorsoAutoNuove = percorsoCartellaBase + "/DB_AutoNuove"
    if os.path.exists(percorsoAutoNuove) == False:
        os.mkdir(percorsoAutoNuove)

    percorsoAutoUsate = percorsoCartellaBase + "/DB_AutoUsate"
    if os.path.exists(percorsoAutoUsate) == False:
        os.mkdir(percorsoAutoUsate)

def GetPercorsoAutoNuove():
    
    return percorsoCartellaBase + "/DB_AutoNuove"

def GetPercorsoAutoUsate():
    
    return percorsoCartellaBase + "/DB_AutoUsate"

