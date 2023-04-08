import smtplib 
import os
import FUNZIONI.procedure as proc

# funzioni 

class Mail:

    def __init__(self, nome_server, porta_server, nome_utente):
        
        self.__DB_Password = "" # path da isnerire, il path dove sta il file con la password
        self.__nomeServer = nome_server
        self.__portaServer = porta_server
        self.__nomeUtente = nome_utente
        self.OttieniPassword()
        

    def SendMail(self,sDest,sObj,sContent):
            
        print("\n Devo mandare una mail a " + sDest)
        
        self.__email = smtplib.SMTP(self.__nomeServer, self.__portaServer)
   
        self.__email.ehlo() 
        self.__email.starttls()
        try: 
            
            self.__email.login(self.__nomeUtente, self.__passwd_utetne)
        
        except ConnectionError:
            print("Errore di connessione")
            
        print("\n Sto inviando...")
        
        message = 'Subject: '+ sObj + '\n\n' + sContent

        self.__email.sendmail(self.__nomeUtente, sDest, message)

        self.__email.quit()
        
        print("Messaggio inviato")

    
    
    def OttieniPassword(self):
                
        letturaFile = 0 

        if os.path.exists(self.__DB_Password): # verifichiamo se c'è quel file (cioè si prende il path e controlla se c'è il file)
            
            # se il file c'è leggilo e decryptalo:

            pwd_Decrypted = proc.DecryptPassword(self.__DB_Password)
            
            self.__passwd_utetne = pwd_Decrypted # e la password sarà quella presente dentro il file decryptata

            letturaFile = 1


            if not len(self.__passwd_utetne) == 16:   # se il file non c'è o per sbaglio non è corretto (non è di 16 caratteri)
                letturaFile = 0


        if letturaFile == 0:

            while letturaFile == 0:
                
                print("\n Inserisci password: ")

                password = proc.hide_input() # nascondiamo la password 

                proc.CryptPassword(password, self.__DB_Password)
                
                self.__passwd_utetne = password # e ora la password che passerà nel login sarà la password che ha dato l'utente
                
                letturaFile = 1
    
    
    
    



            
    
