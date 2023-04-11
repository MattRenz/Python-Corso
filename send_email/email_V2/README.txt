EMAIL_V2


Descrizione:

Decide de mandare l'email al singolo utente usando la password salvata nel file 
inserita da noi manualmente, o se inserire la password manualmente senza leggerla dal file


Utilizzo:

Inserire la propria email per fare il login, inserire la password dentro un file e inserirlo 
dentro la cartella DB_Pswd per fare in modo che verrà letta quando si andra a fare il login. 
Il programma ci chiede se in serire la password manualmente e quindi andare a scriverla da tastiera, 
o se vogliamo usare quella presente dentro il file. Il proseguimento è uguale alle altre versioni, 
ci chiederà l'email del destinatario, l'oggetto e il contenuto e poi inviera l'email

Dipendenze (librerie)

Librerie Utilizzate dal programma: smtplib / sys / re / os


Note: 

Il programma salvera le auto in questo path Windows: "C:\Users\nome utente che ha effetuato l'accesso\Programma_EmailV2"
Appena si esegue il prograamma si andra a creare in automatico la cartella contenente il file con la password 


Possibili errori:

Salvera le cartelle in automatico solo su sistema operativo Windows su sistema operativo Linux o altri bisognerà inserire il path di 
dove si vogliono salvare le cartelle.





