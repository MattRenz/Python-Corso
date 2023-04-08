CONCESSIONARIO V2 

Descrizione: 

Concessionario di Auto e Auto usate  che effetua determinate procedure tra qui:

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


Possibili Errori:

A differenza della versione 1 che una volta che chiudevamo il programma perdeva tutti i file, in questa versione vediamo la persistenza, ovvero 
che alla chiuserà del programma i dati che abbiamo inserito continueranno ad esistere. per questo motivo ci sono due cartelle chiamate DB_Auto_nuove e 
DB_Auto_usate, dobbiamo prendere questi path e inserirli dentro le variabili pathLinuxAutoUsate e pathLinuxAutoNuove nel file (conessonario.py)


Note: 

Dentro il programma sono già salvate delle auto per fare dei test, si consiglia quindi di prendere quel path e inserirlo alla richiesta del programma. 

Il calcolo del valore di un auto è in base ai Km/h percorsi e i vari procedimenti possono essere visti all'intenro del file automobili_usate.py
nella funzione CalcolaValoreAutoUsate() se l'auto ha un certo numero di Km avà un certo prezzo.







