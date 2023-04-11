import mail_class
import re

print("Programma invio mail")


# impostare il server di mail

sNomeServer = "smtp.gmail.com"
iServerPort = 587
sUsername = input("Inserisci la tua email (users): ")
sFilePassword = input("Path dove leggere la password: ")


myMailServer = mail_class.Mail(sNomeServer,iServerPort,sUsername,sFilePassword) # oggetto della classe MAIL

while(1):
    
    sDestinatario = input("Inserisci indirizzo mail destinatario: ")
    
    controllo = r'\b[A-Z a-z 0-9 ._%+-]+@[A-Z a-z 0-9]+\.[A-Z a-z]{2,7}\b' # controllo email
    
    if re.findall(controllo, sDestinatario):
        print("\n Valid Email")
        
        sOggettoMail = input("Inserisci oggetto mail: ")
        sTestoMail = input("Inserisci il testo della mail: ")                                  
                              
        myMailServer.SendMail(sDestinatario,sOggettoMail,sTestoMail) # richiamo funzione SendMail dentro l'oggetto myMailServer che contiene la classe Mail  
    
    else:
        print("Invalid Email")
    

    