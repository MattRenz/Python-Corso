import mail_class
import re
import sys
import os
import CreazioneCartelle 
CreazioneCartelle.CreazioneCartelle()

print("\n Programma invio mail")


# impostare il server di mail

sNomeServer = "smtp.gmail.com"
iServerPort = 587
sUsername = input("Inserire la tua email (users): ")
sFilePassword = CreazioneCartelle.GetPercorsoPswd() + "/pswd.data"


controlloEmailGeneral = r'\b[A-Z a-z 0-9 ._%+-]+@[A-Z a-z 0-9]+\.[A-Z a-z]{2,7}\b'
      
if os.path.exists(sFilePassword):
    
    Oper = input("\n (1 Usa password salvata nel PC, 2 Inserisci manualmente, 3 Esci)")
    
else: 
    Oper = input("\n (2 Inserisci password manualmente, 3 Esci)")

if Oper == "3":
    sys.exit()

if Oper == "1":
    
    Password = None # input utente
    myMailServer = mail_class.Mail(sNomeServer,iServerPort,sUsername, Password, sFilePassword)

    while(1):
        
        sDestinatario = input("\n Inserisci indirizzo mail destinatario: ")
        
        if re.findall(controlloEmailGeneral, sDestinatario):
            print("\n Valid Email")
            
            sOggettoMail = input("\n Inserisci oggetto mail: ")
            sTestoMail = input("\n Inserisci il testo della mail: ")

            myMailServer.SendMail(sDestinatario,sOggettoMail,sTestoMail)       
        
        else:
            print(f'\n Invalid Email. \n e-mail: ({sDestinatario}) non valida')
            
if Oper == "2":

    Password = input(f'\n Inserisci Password collegata a {sUsername}: ')
    with open(sFilePassword, "w") as file:
        file.write(Password)
    sFilePassword = None
    myMailServer = mail_class.Mail(sNomeServer,iServerPort,sUsername,Password,sFilePassword)
    
    while(1):
    
        sDestinatario = input("\n Inserisci indirizzo mail destinatario: ")
        if re.findall(controlloEmailGeneral, sDestinatario):
            print("\n Valid Email")
            
            sOggettoMail = input("\n Inserisci oggetto mail: ")
            sTestoMail = input("\n Inserisci il testo della mail: ")

            myMailServer.SendMail(sDestinatario,sOggettoMail,sTestoMail)       
        else:
            print(f'\n Invalid Email. \n e-mail: ({sDestinatario}) non valida')
            
        
    
    
    