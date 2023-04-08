EMAIL_V1 


Descrizione: 

Programma che manda un email ad un singolo utente, facendo il login con 
la nostra email e leggendo la password per il login da un file. Per inviare un email 
occorre inserire l'email del destinatario, l'oggetto e il contenuto dell'email


Utilizzo: 

avviare il file main.py, inserire la propria email per il login, inserire la password nel file 
mypwd.txt presente nella cartella, in modo che possa successivamente essere letta e usata per il login, 
inserire l'email del destinatario, l'email verrà cotrollata tramite dei principi per la validità dell'email
Inserire l'oggetto e il contenuto dell'email, e aspettare la conferma dell'invio dell'email


Dipendenze: 

Librerie utilizzate dal programma: smtplib / re


Possibili errori:

Modificare i path inserendo i propri percorsi. 
Come sFilePassword (main.py)
Inserire la password dentro il file mypwd.txt sennò non verrà letta nessuna password per il login e andrà in errore