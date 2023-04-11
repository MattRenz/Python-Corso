import os
import sys
import re
import docente as doc
import studenti as stud
import CreazioneCartelle 

CreazioneCartelle.CreazioneCartelle()

pathWindowsDocentiUniversita = CreazioneCartelle.GetPercorsoDocenti()
pathWindowsStudentiUniversita = CreazioneCartelle.GetPercorsoStudenti()

def SalvaDocenti(csDocente):

    sNomeFile = pathWindowsDocentiUniversita + "/" + csDocente.GetIdentificativo() + ".csv" 

    StirngaDocente = doc.docente.CreaDatiDocente(csDocente) 

    file = open(sNomeFile, "w")
    file.write(StirngaDocente) 
    file.close() 

def leggiDocente(sFileDocenti):

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

def SalvaStudenti(csStudente):
    
    sNomeFile = pathWindowsStudentiUniversita + "/" + csStudente.GetMatricola() + ".csv" 
      
    contenutoFile = stud.Studente.CreaDatiStudente(csStudente)
    
    file = open(sNomeFile, "w")
    file.write(contenutoFile)
    file.close()
    
def leggiStudente(sFileStudenti):
    
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
            csStudente = stud.Studente(nome,cognome,mail,matricola, listaVoti)
    else:
        csStudente = stud.Studente(nome,cognome,mail,matricola)
        
    return csStudente
    
    

# SEGRETERIA

print("Segreteria studenti".center(80, "_"))

while(1): 
    Oper = input("\n 1 Sezione Docente, 2 Sezione Studente, 3 Uscita: ")
    
    if Oper == "3":
        sys.exit()   
    
# SEZIONE DOCENTI

    lNuovoDocente = [] # lista di OGGETTI
    
    if Oper == "1":

        print("\n SEZIONE DOCENTI")
        
        while(1):        
            sOperDoce = input("\n Operazione (1 Aggiungi Docente, 2 inserisci corso, 3 Trova corso, 4 Esci)")
    
            if sOperDoce == "4":
                sys.exit()

            # (1) AGGIUNGI DOCENTE
            
            if sOperDoce == "1":
                
                sNome = input("\n Inserisci nome docente: ")
                sCognome = input("\n Inserisci cognome docente: ")
                sIdetnificativo = input("\n Inserisci Identificativo docente: ")
                mail = input(f'\n Mail: ')
                        
                sNuovoDocente = doc.docente(sNome, sCognome, sIdetnificativo, mail) 
                lNuovoDocente.append(sNuovoDocente)
                SalvaDocenti(sNuovoDocente)
   
            # (2) AGGIUNGI CORSO
    
            if sOperDoce == "2": 
                
                sIdetnificativo = input(f'\n Inserisci identificativo: ')
                corso = input(f'\n Aggiungi corso: ')

                listaDocentiUniversita = os.listdir(pathWindowsDocentiUniversita) 
                
                trovaDocente = 0    
                for curfile in listaDocentiUniversita: 
                
                    if curfile == sIdetnificativo + ".csv": 
                      
                        Nuovo_Docente = leggiDocente(curfile) 
                        Nuovo_Docente.AggiungiCorso(corso) 
                        SalvaDocenti(Nuovo_Docente) 
                        
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

                        Nuovo_Docente = leggiDocente(curfile)
                        Nuovo_Docente.CalcolaCorsi()    
                        trovaCorso = 1
                        
                if trovaCorso == 0:
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
                    
                
    # SEZIONE STUDENTI

    if Oper == "2":

        print("\n SEZIONE STUDENTI")

        while(1):        
            sOperStud = input("\n Operazione (1 Aggiungi Studente, 2 inserisci Voto, 3 Calcola media voti, 4 Exit)")

            if sOperStud == "4":
                sys.exit()
            
            # (1) AGGIUNGI STUDENTE
            
            if sOperStud == "1":

                nome = input("Nome: ")
                cognome = input("Cognome: ")
                matricola = input("Matricola: ")
                mail = input(f'\n Mail: ')

                    
                nuovoStudente = stud.Studente(nome,cognome,mail,matricola)
                SalvaStudenti(nuovoStudente)
                  
            # (2) AGGIUNGI VOTO
             
            if sOperStud == "2":
                
                matricola = input("\n Matricola: ")
                voto = int(input("\n Voto: "))
                
                listaStudentiUniverstia = os.listdir(pathWindowsStudentiUniversita)
                
                trovaStudente = 0
                
                for file in listaStudentiUniverstia:
                    
                    if file == matricola + ".csv":
                        
                        nuovo_Studente = leggiStudente(file)
                        nuovo_Studente.AggVoti(voto)
                        SalvaStudenti(nuovo_Studente)
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
                        nuovo_Studente = leggiStudente(file)
                        nuovo_Studente.CalcolaMediaVoti()
        
                                        
                if trovaStudente == 0:
                    print(f'\n Studente non trovato matricola {matricola} non riconosciuta')  
                    
                
            
                     
      

                  
                
                
            
        
        
                        
                
                    
                
                
            
                                                     
                                                     
                                
            
        

    

                    

                    
                    

            
    



