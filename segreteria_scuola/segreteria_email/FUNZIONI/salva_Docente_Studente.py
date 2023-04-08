import studenti as stud
import docente as doc

def SalvaDocenti(csDocente, pathWindowsDocentiUniversita):

    sNomeFile = pathWindowsDocentiUniversita + "/" + csDocente.GetIdentificativo() + ".csv" 

    StirngaDocente = doc.docente.CreaDatiDocente(csDocente) 

    file = open(sNomeFile, "w")
    file.write(StirngaDocente) 
    file.close() 

def SalvaStudenti(csStudente, pathWindowsStudentiUniversita):
    
    sNomeFile = pathWindowsStudentiUniversita + "/" + csStudente.GetMatricola() + ".csv" 
      
    contenutoFile = stud.Studente.CreaDatiStudente(csStudente)
    
    file = open(sNomeFile, "w")
    file.write(contenutoFile)
    file.close()
    