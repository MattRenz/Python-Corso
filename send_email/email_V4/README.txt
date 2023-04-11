EMAIL_V4

Descrizione:


Manda email all'utente, se la password è presente nel file ed è giusta la legge e non la cheiderà più 
altrimenti, chiederà di inserila all'utente, nascondendo  l'input e cryptandola nel momento che la inserisce e decryptandola
nel momento che la legge, cancellerrà il file automaticamente dopo 5 giorni, in modo che l'utente è obbligato a rinserirla



Utilizzo:

Ci chiederà di inserire la nostra email che useremo nel login, la prima volta ci chiederà di inserire anche la password. 
Una volta inserita la password, avvengono due cose che noi non vedremo 1) Crypta la password salvandola cryptata in modo che non sia leggibiel
e 2) Salva la data di creazione del file con la password, così dopo 5 giorni cancellerrà il file automaticamente, e crea anche un file che sarà la chiave di decriptazione da usare quando decripteremo il file Il resto del procedimento è come le versioni precedenti. Inseriremo l'email del destinatario, l'oggetto e il cotennuto e manderà l'email



Dipendenze (librerie)

Librerie Utilizzate dal programma: smtplib / datetime / timedelta / os / sys / re / cryptography.fernet / msvcrt


Note: 

Il programma salvera le auto in questo path Windows: "C:\Users\nome utente che ha effetuato l'accesso\Programma_EmailV4"
Appena si esegue il programma si andra a creare in automatico la cartella contenente il file con la password, e una cartella contenente 
la chiave di criptazione


Possibili errori:

Salvera le cartelle in automatico solo su sistema operativo Windows su sistema operativo Linux o altri bisognerà inserire il path di 
dove si vogliono salvare le cartelle.

