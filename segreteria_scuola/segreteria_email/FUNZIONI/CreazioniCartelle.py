import os

def CartellaBase():
    
    return os.getenv('USERPROFILE') + "/Programma_SegreteriaEmail"

percorsoCartellaBase = CartellaBase()
    
def CreazioneCartelle():
    
    percorsoCartellaBase = os.getenv('USERPROFILE') + "/Programma_SegreteriaEmail"
    if os.path.exists(percorsoCartellaBase) == False:
        os.mkdir(percorsoCartellaBase)
    
    
    percorsoDocenti = percorsoCartellaBase + "/DB_Docenti"
    if os.path.exists(percorsoDocenti) == False:
        os.mkdir(percorsoDocenti)

    percorsoStudenti = percorsoCartellaBase + "/DB_Studenti"
    if os.path.exists(percorsoStudenti) == False:
        os.mkdir(percorsoStudenti)
        
    percorsoPasswordGmail = percorsoCartellaBase + "/DB_Pswd"
    if os.path.exists(percorsoPasswordGmail) == False:
        os.mkdir(percorsoPasswordGmail)

def GetPercorsoDocenti():
    
    return percorsoCartellaBase + "/DB_Docenti"

def GetPercorsoStudenti():
    
    return percorsoCartellaBase + "/DB_Studenti"

def GetPercorsoDBPswd():
    
    return percorsoCartellaBase + "/DB_pswd"


