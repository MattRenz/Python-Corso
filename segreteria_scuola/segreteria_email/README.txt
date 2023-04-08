SEGRETERIA EMAIL 


Descrizione:

Questo prgramma gestisce una segreteria, salvando studenti e docenti e utilizzando i loro attributi per affetturare vari metodi
E' implementata anche la possibilità di mandare email ai docenti o studenti


Utilizzo:

Possiamo eseguire vari metodi, il programma inizialmente ci chiede se vogliamo entrare nella sezione studente o sezione docente
una volta scelto dove entrare possiamo fare diverse procedure

Studenti: 

    1) Inserire studente
    2) Inserire voto a studente 
    3) Calcolare Media voti 
    4) Mandare email personale e vedere tutte le email degli studenti
    5) Mandare email in automatico gli studenti che hanno la media sotto il 18 

Docenti: 

    1) Inserie nuovo docente 
    2) Inserie corso 
    3) Trovare corso 
    4) Mandare email perosnale e vedere tutte le email dei docenti
    

Il programma inizialemente ci chiederà di inserire l'email che poi useremo per il login quando invieremo le email, ci chiederà anche 
la password che inseriremo una sola volta, se la password poi rimane salvata nel file verà usata sempre quella presente nel file. 

Finito di impostare password ed email per il login, possiamo usare i vari metodi delle classi docenti e studenti


Dipendenze (librerie):

Le librerie che usa questo progrmma sono: smtplib / os / sys / re 


Possibili errori

Bisogna inserire il proprio path di DB_Password, DB_Studenti, DB_Docenti, nelle varabile richieste, ubicazione variabili:

self.__DB_Password in (mail.py, segreteria.py, studenti.py e salvaPassword) Path di salvataggio password

pathWindowsDocentiUniversita Path dove veranno salvati i docenti, inserire il path nei file:
segreteria.py / get.Email.py / leggi_Docenti_Studenti.py / leggiEmail_Docenti_Studenti.py / salva_Docente_Studente.py

pathWindowsStudentiUniversita Path dove veranno salvati gli studenti, inserire il path nei file: 
segreteria.py / get.Email.py / leggi_Docenti_Studenti.py / leggiEmail_Docenti_Studenti.py / salva_Docente_Studente.py


Note: 

All'intenro della cartella FUNZIONI sono presenti tutte le funzioni e procedure che vengono richiamate dentro segreteria.py

ELIMINARE I FILE .gitgnore prima di iniziare l'esecuzione del programma


