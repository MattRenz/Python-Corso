EMAIL_V3


Descrizione:

Manda l'email all'utente se la password è salvata nel file ed è uguale a 16 caratteri (lunghezza predefinita)
userà quella dentro il file, quindi ci chiederà di inserirla e la salverà dentro il file per sempre e non ci chiederà 
più di inserirla. Altrimenti se il file non è presente ci chiederà di inserila da tastiera. 


Utilizzo:

Ci chiederà di isnerire la nostra email che userà poi per fare il login.
Nel caso iniziale la password non è presente nel file, quindi inseriremo anche la password che useremo poi nel login.
Nel caso la password è presente allora la leggera tramite il file
Il procedimento è uguale alle versioni precedenti, ci chiederà l'email del destinatario, l'oggetto, e il contenuto e 
poi inviera l'email


Dipendenze (librerie)

Librerie Utilizzate dal programma: smtplib / os / re


Possibili errori:

Modifciare inserendo il proprio path a self.__DB_Password(mail_class.py)


