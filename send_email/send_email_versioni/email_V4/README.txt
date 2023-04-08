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


Possibili errori:

I possibili errori sono i soliti errori di path da inserire nelle variabili vuote, su self.__DB_Password(mail_class.py)
e su file (FUNZIONI.procedure.py), e anche all'interno del file procedure, la variabile privateKey, deve contenere il path di dove andremo a salvare il file con la chiave dentro

INSERIRE TUTTI I PATH IN MODO CORRETTO PRIMA DI ESEGUIRE IL PROGRAMMA

