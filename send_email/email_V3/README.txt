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


Note: 

Il programma salvera le auto in questo path Windows: "C:\Users\nome utente che ha effetuato l'accesso\Programma_EmailV3"
Appena si esegue il prograamma si andra a creare in automatico la cartella contenente il file con la password 


Possibili errori:

Salvera le cartelle in automatico solo su sistema operativo Windows su sistema operativo Linux o altri bisognerà inserire il path di 
dove si vogliono salvare le cartelle.

