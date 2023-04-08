import mail_class
import FUNZIONI.procedure as proc
import datetime
import re



print("\n Programma invio mail")

pathFIle = "" # questo è il path dove andremo a inserire il file "032812.data" contentete la password


# impostare il server di mail

sNomeServer = "smtp.gmail.com"
iServerPort = 587
sUsername = input("Inserire la tua email (users): ")
controlloEmailGeneral = r'\b[A-Z a-z 0-9 ._%+-]+@[A-Z a-z 0-9]+\.[A-Z a-z]{2,7}\b'
 
# data entrata utente 

entrataNelProgramma = datetime.datetime.now()
dateCreazioneFile = proc.dataCreazioneFile(pathFIle)

proc.EliminaFile(entrataNelProgramma) 
    
myMailServer = mail_class.Mail(sNomeServer,iServerPort, sUsername)

while(1):

    while(1):
        
        destinatario = input("\n Destinatario: ")

        if re.findall(controlloEmailGeneral, destinatario):

            ogg = input("Ogg: ")
            contenuto = input("Contenuto: ")
            myMailServer.SendMail(destinatario, ogg, contenuto)

        else: 

            print(f'\n Invalid Email. \n e-mail: ({destinatario}) non valida')

