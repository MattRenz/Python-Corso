import os

def CartellaBase():
    
    return os.getenv('USERPROFILE') + "/Programma_EmailV3"

percorsoCartellaBase = CartellaBase()
    
def CreazioneCartelle():
    
    percorsoCartellaBase = os.getenv('USERPROFILE') + "/Programma_EmailV3"
    if os.path.exists(percorsoCartellaBase) == False:
        os.mkdir(percorsoCartellaBase)
    
    
    percorsoDB_pswd = percorsoCartellaBase + "/DB_Pswd"
    if os.path.exists(percorsoDB_pswd) == False:
        os.mkdir(percorsoDB_pswd)
        
        

def GetPercorsoPswd():
    
    return percorsoCartellaBase + "/DB_Pswd"
