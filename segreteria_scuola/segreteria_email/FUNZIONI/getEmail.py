def getEmail(filestudenti, pathWindowsStudentiUniversita):
    
    listaemail = []
    
    nomefile = pathWindowsStudentiUniversita + "/" + filestudenti
    
    file = open(nomefile)
    
    strfile = file.readline()
    
    filesplit = strfile.split(";")
    
    nome = filesplit[0]
    cognome = filesplit[1]
    mail = filesplit[2]
    
    stringa = f'{nome} {cognome} = {mail}'
    
    listaemail.append(stringa)
    
    return listaemail

def getEmailDocenti(filedocenti, pathWindowsDocentiUniversita):
    
    if filedocenti != ".gitignore":
        
        listaemail = []
        
        nomefile = pathWindowsDocentiUniversita + "/" + filedocenti
        
        file = open(nomefile)
        
        strfile = file.readline()
        
        filesplit = strfile.split(";")
        
        nome = filesplit[0]
        cognome = filesplit[1]
        mail = filesplit[3]
        
        stringa = f'{nome} {cognome} = {mail}'
        
        listaemail.append(stringa)
        
        return listaemail
        
    
    
    