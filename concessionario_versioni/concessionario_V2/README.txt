CONCESSIONARIO V2 

Descrizione: 

Concessionario di Auto nuove e Auto usate che effetua determinate procedure tra qui:

AUTO NUOVE:

	Procedure: 

		1) inserimento auto nuova
		2) Aggiungi Optional
		3) Rimuovi Optional
		4) Calcola Valore Auto (in base a l'anno di uscita e il prezzo di listino)

	Archivi:
		
		1) Stampa Scheda auto
		2) Trova Optional
		3) Trova Targhe
		4) Trova auto da Carburante

----------------------------------------------------

AUTO USATE:

	Procedure: 
		
		1) inserimento auto nuova
		2) Aggiungi Optional
		3) Rimuovi Optional
		3) Calcola valore Auto (in base al numero di Km) 
		 
	Archivi:

		1) Stampa scheda auto 
		2) Trova Optional 
		3) Trova targhe 
		4) Trova auto da Carburante 
	

Utilizzo:

La classe padre è la classe veicoli che è padre delle clssi automobili e moto. L'utente può sceglire l'operazione da fare e in base 
all'operazione scelta il programma richieamera le procedure dalle varie classi 


Dipendenze:

Le librerie utilizzate in questo programma sono:  sys / os / datetime


Note: 

Il programma salvera le auto in questo path Windows: "C:\Users\nome utente che ha effetuato l'accesso\/Programma_Concessionario"
Appena si esegue il prograamma si andranno a creare in automatico i DB per l'auto nuove e usate

Il calcolo del valore di un auto è in base ai Km/h percorsi e i vari procedimenti possono essere visti all'intenro del file automobili_usate.py
nella funzione CalcolaValoreAutoUsate() se l'auto ha un certo numero di Km avà un certo prezzo.


Possibili errori:

Salvera le cartelle in automatico solo su sistema operativo Windows su sistema operativo Linux o altri bisognerà inserire il path di 
dove si vogliono salvare le cartelle.






