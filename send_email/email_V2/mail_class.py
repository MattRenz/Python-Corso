import smtplib # libreria utilizzata per inviare email

class Mail:

    def __init__(self, nome_server, porta_server, nome_utente, passwd_uente, Filepwd):
        
        self.__nomeServer = nome_server
        self.__portaServer = porta_server
        self.__nomeUtente = nome_utente
    
        if Filepwd is None:
            self.__passwd_uente = passwd_uente
        else:
            file = open(Filepwd, "r")
            self.__passwd_uente = file.readline()
            file.close()
        
    def SendMail(self,sDest,sObj,sContent):
            
        print("\n Devo mandare una mail a " + sDest)
        
        self.__email = smtplib.SMTP(self.__nomeServer, self.__portaServer)
   
        self.__email.ehlo() 
        self.__email.starttls()
        self.__email.login(self.__nomeUtente, self.__passwd_uente)
                    
        print("\n Sto inviando...")
        
        message = 'Subject: '+ sObj + '\n\n' + sContent

        self.__email.sendmail(self.__nomeUtente, sDest, message)

        self.__email.quit()
        
        print("Messaggio inviato")
    
