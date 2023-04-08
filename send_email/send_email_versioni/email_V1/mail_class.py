import smtplib # libreria utilizzata per inviare email

class Mail:

    def __init__(self,nome_server,porta_server,nome_utente,passw_utente):
        
        self.__nomeServer = nome_server
        self.__portaServer = porta_server
        self.__nomeUtente = nome_utente

        # apri un file in modalità lettura di nome passw_utente
        f = open(passw_utente, "r")
        self.__pwdUtente = f.readline() # leggi la prima linea del file
        f.close()
        

    def SendMail(self, sDest,sObj, sContent):
            print("Devo mandare una mail a " + sDest)
            
            self.__email = smtplib.SMTP(self.__nomeServer, self.__portaServer)
        
            # smtplib.SMTP in python fornisce un interfaccia per inviare e-mail. 
            
            self.__email.ehlo() 
            
            # ehlo() viene utilizzato per iniziare la comunicazione con il server di posta elettronica e identificare il mittente dell'e-mail.
            # invia una richiesta al server di posta elettronica, il server riponde con il codice di stato 250 se la conessione è stata stabilita corettamente
            
            self.__email.starttls()
            
            # starttls() il metodo avvia una negoziazione di sicurezza con il server di posta elettronica, per cittografare la connessione e proteggere i dati scambiati durant la comunicaizone
            # tutti i dati scambiati tra client e il server di posta elettronica saranno cittografati, fornendo una maggiore sicurezza


            self.__email.login(self.__nomeUtente, self.__pwdUtente)
            
            # login() viene utilizzato per autentcarsi su un server di posta elettronica utilizzando il protocollo SMTP
            # richiede due parametri, l'indirizzo email dell'account e la password
            
            print("Sto inviando...")
            
            message = 'Subject: '+ sObj + '\n\n' + sContent
    
            self.__email.sendmail(self.__nomeUtente, sDest, message)
            
            # sendmail() invia un messaggio di posta elettronica. Richiede 3 parametri, l'indirizzo email del mittente, l'indirizzo email del destinatario, e il messaggio 
            
            self.__email.quit()
            
            # quit() chiude la connessione con il server di posta elettronica dopo aver completato l'invio di messaggi di posta elettronica 


