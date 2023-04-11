import os
import sys
import re

# classi 
import docente as doc
import studenti as stud
import mail

# funzioni
import FUNZIONI.CreazioniCartelle as creazioneCartelle
creazioneCartelle.CreazioneCartelle()
creazioneCartelle.GetPercorsoDocenti()
import FUNZIONI.leggi_Docenti_Studenti as leggi
import FUNZIONI.salva_Docente_Studente as salva
import FUNZIONI.leggiEmail_Docenti_Studenti as leggiEmail
import FUNZIONI.getEmail as getmail

pathWindowsDocentiUniversita = creazioneCartelle.GetPercorsoDocenti()
pathWindowsStudentiUniversita = creazioneCartelle.GetPercorsoStudenti()
                                    

sNomeServer = "smtp.gmail.com"
iServerPort = 587
sUsername = input("Inserire la tua email (users): ")

myMailServer = mail.Mail(sNomeServer,iServerPort, sUsername)
    
    
controlloEmailGeneral = r'\b[A-Z a-z 0-9 ._%+-]+@[A-Z a-z 0-9]+\.[A-Z a-z]{2,7}\b'
controlloEmailGmail = r'\b[A-Z a-z 0-9 ._%+-]+@[gmail]+\.[A-Z a-z]{2,7}\b'

while(1): 
    
    print("\n SEGRETERIA STUDENTI")
    
    Oper = input("\n 1 Sezione Docente, 2 Sezione Studente, 3 Uscita: ")
    
    if Oper == "3":
        sys.exit()   
    
    
# SEZIONE DOCENTI

    lNuovoDocente = [] 

    if Oper == "1":

        print("\n SEZIONE DOCENTI")
        
        while(1):        
            sOperDoce = input("\n Operazione (1 Aggiungi Docente, 2 inserisci corso, 3 Trova corso, 4 Manda email personale, 5 Esci): ")
    
            if sOperDoce == "5":
                sys.exit()

            # (1) AGGIUNGI DOCENTE
            
            if sOperDoce == "1":
                
                sNome = input("\n Nome docente: ")
                sCognome = input("\n Cognome docente: ")
                sIdetnificativo = input("\n Identificativo docente: ")                   
                while(1):
                    email = input("\n Email: ") 

                    if re.findall(controlloEmailGeneral, email):
                        sNuovoDocente = doc.docente(sNome, sCognome, sIdetnificativo, email) 
                        lNuovoDocente.append(sNuovoDocente)
                        salva.SalvaDocenti(sNuovoDocente, pathWindowsDocentiUniversita)
                        break
                    else:
                        print(f'Email non valida \n email: ({email}) non valida')

            # (2) AGGIUNGI CORSO
    
            if sOperDoce == "2": 
                
                sIdetnificativo = input(f'\n Inserisci identificativo: ')
                corso = input(f'\n Aggiungi corso: ')

                listaDocentiUniversita = os.listdir(pathWindowsDocentiUniversita) 
                
                trovaDocente = 0    
                for curfile in listaDocentiUniversita: 
                
                    if curfile == sIdetnificativo + ".csv": 
                    
                        Nuovo_Docente = leggi.leggiDocente(curfile, pathWindowsDocentiUniversita)
                        Nuovo_Docente.AggiungiCorso(corso) 
                        salva.SalvaDocenti(Nuovo_Docente, pathWindowsDocentiUniversita) 
                        
                        trovaDocente = 1
                        
                if trovaDocente == 0:
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
                else:
                    print("\n Corso aggiunto correttamente")

            # (3) TROVA CORSO

            if sOperDoce == "3":

                print("\n Inserisci identificativo del docente per guardare quali corsi insegna")

                sIdetnificativo = input(f'\n Inserisci identificativo: ')

                listaDocentiUniversita = os.listdir(pathWindowsDocentiUniversita)

                trovaCorso = 0
                for curfile in listaDocentiUniversita:

                    if curfile == sIdetnificativo + ".csv"  : 

                        Nuovo_Docente = leggi.leggiDocente(curfile, pathWindowsDocentiUniversita)
                        Nuovo_Docente.CalcolaCorsi()    
                        trovaCorso = 1
                        
                if trovaCorso == 0:
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
                    
            # (4) MANDA EMAIL 
            
            if sOperDoce == "4":
                
                while(1):
                 
                    oper = input("(1 manda email, 2 vedi email)")
                    
                    if oper == "1":
                    
                        listaDocentiUniverstia = os.listdir(pathWindowsDocentiUniversita)
                        
                        destinatario = input("\n (1 exit, Inserisci indirizzo mail destinatario: )")
                        
                        
                        for docente in  listaDocentiUniverstia: 
                                                    
                            emailStundeti = leggiEmail.LeggiEmailDocenti(docente, pathWindowsDocentiUniversita)
                            
                            if destinatario == emailStundeti:
                                
                                oggettoMail = input("\n Inserisci oggetto mail: ")
                                testoMail = input("\n Inserisci il testo della mail: ")
                
                                myMailServer.SendMail(destinatario,oggettoMail,testoMail)
  
    

                    if oper == "2":
                        
                        listaDocentiUniverstia = os.listdir(pathWindowsDocentiUniversita)
                        nmEmail = 1
                        for docente in listaDocentiUniverstia:
                            
                            email = getmail.getEmailDocenti(docente, pathWindowsDocentiUniversita)
                            
                            for e in email:
                                
                                print(f'{nmEmail}) {e}')
                                nmEmail +=1
                            
                                                            
    # SEZIONE STUDENTI

    if Oper == "2":

        print("\n SEZIONE STUDENTI")

        while(1):        
            sOperStud = input("\n Operazione (1 Aggiungi Studente, 2 inserisci Voto, 3 Calcola media voti, 4 Manda email personale, 5 Exit)")

            if sOperStud == "5":
                sys.exit()
            
            # (1) AGGIUNGI STUDENTE
            
            if sOperStud == "1":

                nome = input("Nome: ")
                cognome = input("Cognome: ")
                                                        
                while(1):
                    email = input("Email: ") 

                    if re.findall(controlloEmailGeneral, email):
                        matricola = input("Matricola: ")                
                        nuovoStudente = stud.Studente(nome,cognome,matricola,email)
                        salva.SalvaStudenti(nuovoStudente, pathWindowsStudentiUniversita)
                        break
                    else:
                        print(f'Email non valida \n email: ({email}) non valida')
        
            # (2) AGGIUNGI VOTO
            
            if sOperStud == "2":
                
                matricola = input("\n Matricola: ")
                voto = int(input("\n Voto: "))
                
                listaStudentiUniverstia = os.listdir(pathWindowsStudentiUniversita)
                
                trovaStudente = 0
                
                for file in listaStudentiUniverstia:
                    
                    if file == matricola + ".csv":
                        
                        nuovo_Studente = leggi.leggiStudente(file, pathWindowsStudentiUniversita)
                        nuovo_Studente.AggVoti(voto)
                        salva.SalvaStudenti(nuovo_Studente, pathWindowsStudentiUniversita)
                        trovaStudente = 1
                        
                if trovaStudente == 0:
                    print(f'\n Studente non trovato matricola {matricola} non riconosciuta') 
                else:
                    print("\n Voto aggiunto correttamente")                      
                    
            # (3) CALCOLA MEDIA
            
            if sOperStud == "3":
                
                smatricola = input("\n Matricola: ")
                
                listaStudentiUniverstia = os.listdir(pathWindowsStudentiUniversita)
                
                trovaStudente = 0
                for file in listaStudentiUniverstia:
                    
                    if file == smatricola + ".csv":
                        trovaStudente = 1
                        nuovo_Studente = leggi.leggiStudente(file, pathWindowsStudentiUniversita)
                        nuovo_Studente.CalcolaMediaVoti()
                        
                        # manda email se sotto il 18 e con almeo 4 voti 
                        if nuovo_Studente.CalcolaMediaVoti() < 18 and len(nuovo_Studente.GetListaVoti()) > 4:
                            
                            email = leggiEmail.LeggiEmailStudenti(file, pathWindowsStudentiUniversita)
                            myMailServer.SendMailMedia(email)
                            
                    
                if trovaStudente == 0:
                    print(f'\n Studente non trovato matricola {matricola} non riconosciuta')  
                    
            # (4) MANDA EMAIL
                
            if sOperStud == "4":
                    
                while(1):
                    
                    oper = input("(1 manda email, 2 vedi email)")
                    
                    if oper == "1":
                        
                        listaStudentiUniverstia = os.listdir(pathWindowsStudentiUniversita)
                        
                        destinatario = input("\n (1 exit, Inserisci indirizzo mail destinatario: )")
                        
                        if destinatario == "1":
                            sys.exit()
                        
                        for studente in listaStudentiUniverstia: 
                                                    
                            emailStundeti = leggiEmail.LeggiEmailStudenti(studente, pathWindowsStudentiUniversita)
                            
                    
                            if destinatario == emailStundeti:
                                
                                oggettoMail = input("\n Inserisci oggetto mail: ")
                                testoMail = input("\n Inserisci il testo della mail: ")
                
                                myMailServer.SendMail(destinatario,oggettoMail,testoMail)
  
  
                    if oper == "2":
                        
                        listaStudentiUniverstia = os.listdir(pathWindowsStudentiUniversita)
                        emailNm = 1
                        
                        for studente in listaStudentiUniverstia:
                            
                            email = getmail.getEmail(studente, pathWindowsStudentiUniversita)
                        
                            for e in email:
                                
                                print(f'{emailNm}) {e}')
                                emailNm += 1
                                
                                
                                
                                
                                

