import studente as stud
import sys
import FUNZIONI.SalvaSuServer as saveStudentServer


# print("Programma di prova di httpclient")
# myHttp = httpclient.MyHttpClient("127.0.0.1",8081) # ping su linux, o sito web (www)
# iret = myHttp.SendHTTPData("/index.html", "") # o index html, o url della pagina
# print(iret)
# sys.exit()


while(1):        
    sOperStud = input("\n Operazione (1 Aggiungi Studente) ")

    if sOperStud == "5":
        sys.exit()

    # (1) AGGIUNGI Studente
    
    if sOperStud == "1":
        
        inserimentoOK = 0
        
        while inserimentoOK == 0:
            sNome = input("\n Nome studente: ")
            sCognome = input("\n Cognome studente: ")
            matricola= input("\n Matricola studente: ")     
            email = input("\n Email: ")    

            sNuovoStudente = stud.Studente(sNome, sCognome, email, matricola) 
        
            sNuovoStudente.stampaScheda()
            inserimentoOK = 1

            operSave = input("\n Confermi i dati? (si, no)").lower()

            if operSave == "si":
    
               iret = saveStudentServer.SalvaStudentiSuServer(sNuovoStudente)
               
               print(F'Esito operazione: {iret}')

            elif operSave == "no":
                inserimentoOK = 0
            