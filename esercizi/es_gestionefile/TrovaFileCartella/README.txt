TROVA FILE o CARTELLA

Descrizione: 

Questo programma dato un path, troverà un file o una cartella secondo il parametro che gli passiamo, se chiediamo la ricerca 
per estenzione, ci chiederà l'estenzione del file che stiamo cercando e successivamente ci tirerà fuori tutti i file con quell'estenzione.
Se stiamo cercando per nome (cartella, file) ci chiederà il nome della ricerca, e successivamente ci tirera fuori tutti i file o cartelle con 
quel nome


Utilizzo:

    1) Scrivere se stiamo cercando per nome o per estenzione

    2) Inserie il path della cartella su cui stiamo cercando

    3) Inserire la ricerca del file che vogliamo trovare

    Risultato: 
    Restituisce tutti i file/cartelle con l'estenzione o nome richiesto.


Dipendenze:

Le librerie utilizzate in questo programma sono: os / sys


Possibili Errori:

Controllare bene l'inserimento del path, in caso stiamo su sistema operativo Windows python non
riconoscera (\) come separatore del path, quindi va cambiato nel seguente modo (\\), inserendo 
due separatori invece di uno.


Inserie dei parametri validi, qunado il programma ci chiese se stiamo cercando per nome o per estenzione

Inserire un path valido


Note: 

Nell cartella è già presente una cartella chiamata "CartellaDiFile" dove è possibile fare delle prove, copiando 
quel path e inserendolo alla richiesta del programma.








