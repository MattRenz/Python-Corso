def LeggiEmailStudenti(sFileStudenti, pathWindowsStudentiUniversita):
    
    nomeFile = pathWindowsStudentiUniversita + "/" + sFileStudenti
    
    file = open(nomeFile, "r")
    sFile = file.readline()
    sFileSplit = sFile.split(";")
    mail = sFileSplit[2]
    
    return mail
    
def LeggiEmailDocenti(sFileDocenti, pathWindowsDocentiUniversita):
    
    nomeFile = pathWindowsDocentiUniversita + "/" + sFileDocenti
    
    file = open(nomeFile, "r")
    sFile = file.readline()
    sFileSplit = sFile.split(";")
    mail = sFileSplit[3]
    
    return mail
 