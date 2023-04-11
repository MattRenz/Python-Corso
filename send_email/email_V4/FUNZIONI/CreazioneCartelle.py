import os

def CartellaBase():
    
    return os.getenv('USERPROFILE') + "/Programma_EmailV4"

percorsoCartellaBase = CartellaBase()
    
def CreazioneCartelle():
    
    percorsoCartellaBase = os.getenv('USERPROFILE') + "/Programma_EmailV4"
    if os.path.exists(percorsoCartellaBase) == False:
        os.mkdir(percorsoCartellaBase)
    
    
    percorsoDocenti = percorsoCartellaBase + "/DB_Pswd"
    if os.path.exists(percorsoDocenti) == False:
        os.mkdir(percorsoDocenti)
        
    percorsoDB_Key = percorsoCartellaBase + "/DB_Key"
    if os.path.exists(percorsoDB_Key) == False:
        os.mkdir(percorsoDB_Key)
        

def GetPercorsoPswd():
    
    return percorsoCartellaBase + "/DB_Pswd"

def GetPercorsoKey(): 
    
    return percorsoCartellaBase + "/DB_Key"
