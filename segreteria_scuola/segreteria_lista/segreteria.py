
import docente as doc
import studente as stud

import sys

lListaStudentiUniversita = []

listaDocentiUniversita = []

print("Segreteria studenti".center(80, "_"))

while(1):
        
    Oper = input("\n 1 Sezione Docente, 2 Sezione Studente, 3 Uscita: ")
    
    if Oper == "3":
    
        sys.exit()   
    
    # DOCENTI
    
    if Oper == "1":
    
        while(1):
        
            sOperDoce = input("\n Operazione (1 Aggiungi Docente, 2 inserisci corso, 3 stampa corsi, 4 Trova corso, 5 Uscita: )")
    
    
        # stampa docente 
    
            if sOperDoce == "1":
                
                sNome = input("\n Inserisci nome docente: ")
                sCognome = input("\n Inserisci cognome docente: ")
                sIdetnificativo = input("\n Inserisci Identificativo docente: ")
                mail = input(f'\n Mail: ')
    
                sNuovoDocente = doc.docente(sNome, sCognome, sIdetnificativo, mail) # qui richiamo la classe studente e gli assegno gli input dell'utente che per lui corrispondono a gli attibuti della classe 
    
                sNuovoDocente.MostraDocente()
                listaDocentiUniversita.append(sNuovoDocente)
    
        # aggiungi corso
    
            if sOperDoce == "2": 
            
                sIdetnificativo = input(f'\n Inserisci identificativo: ')
    
                corso = input(f'\n Inserisci corso: ')
    
                trovaDocente = 0
    
                for doc in listaDocentiUniversita:
                
                    if doc.GetIdentificativo() == sIdetnificativo:
                    
                        doc.AggiungiCorso(corso)
    
                        trovaDocente = 1
    
                if trovaDocente == 0:
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
    
                else:
                    print("\n Corso aggiunto correttamente")
    
    
        # stampa corso 
    
            if sOperDoce == "3":
            
                sIdetnificativo = input(f'\n Inserisci identificativo: ')
    
                trovaDocente = 0
    
                if doc in listaDocentiUniversita:
                
                    if doc.GetIdentificativo() == sIdetnificativo:
                    
                        doc.CalcolaCorsi()
    
                        trovaDocente = 1
    
                if trovaDocente == 0:
                
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
    
    
            if sOperDoce == "4":
            
                trovaCoroso = input("Nome Corso: ").lower()

                
                for corsoLower in doc.GetCorsi():

                    corsoLower = corsoLower.lower()
            
                    corsoTrovato = 0

                    if trovaCoroso == corsoLower:
                    
                            print(f'\n corso: {trovaCoroso} insengato da {sNome} {sCognome} identificativo: {sIdetnificativo}')
                    
                            corsoTrovato = 1

                    if corsoTrovato == 0:

                        print("Corso non trovato")

            if sOperDoce == "5":
            
                sys.exit()
    
    
    # STUDENTI


    if Oper == "2":
    
        while(1):
                
            sOperStud = input("\nOperazione (1 Aggiungi Stuente, 2 Inserisci Voto, 3 Stampa Media, 4 Uscita: )")
        
        # aggiungi studente
    
            if sOperStud == "1":
                
                sNome = input("\n Inserisci nome studente: ")
                sCognome = input("\n Inserisci cognome studente: ")
                sMatricola = input("\n Inserisci matricola studente: ")
                mail = input(f'\n 1Inserisci mail: ')
    
                sNuovoStudente = stud.studente(sNome,sCognome,sMatricola, mail) # qui richiamo la classe studente e gli assegno gli input dell'utente che per lui corrispondono a gli attibuti della classe 
    
                sNuovoStudente.ControlloEmail()
                sNuovoStudente.MostraStudente()
                lListaStudentiUniversita.append(sNuovoStudente)
                
        # aggiungivoto
    
            if sOperStud == "2":
                sMatricola = input("\n Inserisci matricola:")
                
                sVoto = input("\n Inserisci voto:")
                iVoto = int(sVoto)
                
                iTrovatoStudente = 0
                
                for stud in lListaStudentiUniversita:
                    
                    if stud.GetMatricola() == sMatricola:
                        
                        stud.AggiungiVoto(iVoto) # con stud. richiamiamo i vari metodi presenti nella classe è un istanza/oggetto della classe studente
                        
                        iTrovatoStudente = 1
                        
                if iTrovatoStudente == 0:
                
                    print(f'\n Attenzione, studente non trovato \n Matricola {sMatricola} non riconosciuta')
                else:
                    
                    print("\n Voto aggiunto correttamente".upper())
            
        # calcola media
    
            if(sOperStud == "3"):
                
                sMatricola = input("\n Inserisci matricola:")
                
                iTrovatoStudente = 0
                
                for stud in lListaStudentiUniversita:
                    
                    if stud.GetMatricola() == sMatricola:
                        
                        stud.CalcolaMediaVoti()
                        
                        iTrovatoStudente = 1
                        
                if iTrovatoStudente == 0:
                    print(f'\n Attenzione, studente non trovato \n Matricola {sMatricola} non riconosciuta')
                    
                else:
                    print("\n Voto aggiunto correttamente")
    
            if sOperStud == "4":
            
                sys.exit()
                
                
    