import studenti as stud
import docente as doc


def leggiDocente(sFileDocenti, pathWindowsDocentiUniversita):

    sNomeFile = pathWindowsDocentiUniversita + "/" + sFileDocenti
    
    file = open(sNomeFile, "r") 
    SringaDocente_DalFile = file.readline() 
    file.close() 

    SringaDocente_DalFile_split = SringaDocente_DalFile.split(";")

    if SringaDocente_DalFile_split[len(SringaDocente_DalFile_split) -1] == '': 
        SringaDocente_DalFile_split = SringaDocente_DalFile_split[0:len(SringaDocente_DalFile_split)-1]
    
    nome = SringaDocente_DalFile_split[0] 
    cognome = SringaDocente_DalFile_split[1] 
    Idetnificativo = int(SringaDocente_DalFile_split[2]) 
    mail = SringaDocente_DalFile_split[3]

    listaVotiVuota = []
    
    if len(SringaDocente_DalFile_split) > 4: 

        for corso in SringaDocente_DalFile_split[4:]:
            listaVotiVuota.append(corso)
            csDocente = doc.docente(nome,cognome,Idetnificativo,mail,listaVotiVuota)
    else:
        csDocente = doc.docente(nome, cognome, Idetnificativo, mail)
    
    return csDocente
    
def leggiStudente(sFileStudenti, pathWindowsStudentiUniversita):
    
    nomefile = pathWindowsStudentiUniversita + "/" + sFileStudenti
    
    file = open(nomefile, "r")
    stringaFile = file.readline()
    file.close()
    

    stringaFileSplit = stringaFile.split(";")
    
    if stringaFileSplit[len(stringaFileSplit) -1] == '': 
        stringaFileSplit = stringaFileSplit[0:len(stringaFileSplit)-1]
    

    nome = stringaFileSplit[0]
    cognome = stringaFileSplit[1]
    mail = stringaFileSplit[2]
    matricola = stringaFileSplit[3]
    
    listaVoti = []
    
    if len(stringaFileSplit) > 4:
        
        for voti in stringaFileSplit[4:]:
            
            listaVoti.append(voti)
            csStudente = stud.Studente(nome,cognome,matricola, mail, listaVoti)
    else:
        csStudente = stud.Studente(nome,cognome,matricola, mail)
        
    return csStudente
