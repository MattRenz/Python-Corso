import studente as stud
import sys
import FUNZIONI.SalvaSuServer as saveStudentServer

while(1):        
    sOperDoce = input("\n Operazione (1 Aggiungi Studente) ")

    if sOperDoce == "5":
        sys.exit()

    # (1) AGGIUNGI Studente
    
    if sOperDoce == "1":
        
        inserimentoOK = 0
        
        while inserimentoOK == 0:
            sNome = input("\n Nome studente: ")
            sCognome = input("\n Cognome studente: ")
            matricola= input("\n Matricola studente: ")     
            email = input("\nEmail: ")    

            sNuovoStudente = stud.Studente(sNome, sCognome, email, matricola) 
        
            sNuovoStudente.stampaScheda()
            inserimentoOK = 1

            operSave = input("\n Confermi i dati? (si, no)").lower()

            if operSave == "si":
      
                saveStudentServer.SalvaStudentiSuServer(sNuovoStudente)
                
            elif operSave == "no":
                inserimentoOK = 0

        
            