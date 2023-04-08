SEGRETERIA SERVER V2


Descrizione:

Questo progrmma gestisce una segreteria lato client e server, gestisce la risposta che il server manda, e l'input che manda l'utente
In segreteria, manderemo l'input di una segreteria come per esempio aggiungere uno studente, nome, cognome, matricola, email. Una volta
inseriti i dati e confermati, la funzione SalvaSulServer() richiama la classe MyHttpClient che invia la stringa prefermoata (dentro la classe studente) 
al server, dentro la classe MyHttpClient, Avremo anche la risposta del server (200) sr la connessione è andata a buon fine e 500 se non è andata
Dentro la classe testHTTPServer_RequestHandler, invece avremo la parte dedicata al server. Dove potremmo andare su google e vedere la risposta visiva da una 
pagina web 


Utilizzo:

    1) Invio dati dell'utente (input)
    2) Invio stringa con dati al server



Dipendenze (librerie):

Le librerie che usa questo progrmma sono: sys / http.server / http.client


Note:

Per far eseguire il programma mandare in esecuzione contemporaneamente il file httpserverSegreteria.py e segreteria.py









