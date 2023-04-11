import sys
import os
from datetime import datetime, timedelta
import FUNZIONI.CreazioneCartelle as creazioneCartelle

file = creazioneCartelle.GetPercorsoPswd() + "/pswd.data"
       
 
# ELIMINAZIONE AUTOMATICA FILE
        
def dataCreazioneFile(file):

    if os.path.isfile(file): # se il file esiste 

        creazioneFile = os.path.getctime(file) 
        dataDiCreazioneFile = datetime.fromtimestamp(creazioneFile) # data creazione del file 

        return dataDiCreazioneFile # il ritorno di questa funzione è la data di creazione del file 
# return --> data crezione file 

def EliminaFile(DataEntrataNelProgramma):

    if os.path.exists(file): # se il file esiste 

        creazioneFile = os.path.getctime(file) # restituisci la data di creazione del file 
        dataDiCreazioneFile = datetime.fromtimestamp(creazioneFile) # convertila in un formato data leggibile 

        if (DataEntrataNelProgramma - dataDiCreazioneFile) >= timedelta(days=5): 
            
            # se la differenza, tra la data di entra nel programma e la data di creazione del file è maggiore di 5 giorni (days=5): 
    
            # esempio: 
            
                # if 2023/02/28 - 2023/02/10 = 18 giorni >= 5 ? si --> elimina il file (se esiste)
    
            if os.path.exists(file): # entra in qeusta condizione che verifica se il file esiste 

                os.remove(file) # se esiste rimuovilo 
                

# NASCONDI INPUT (*)

def hide_input():

    # WINDOWS 

    if os.name == 'nt': # verifica se il sistema opertivo è Windows
        
        import msvcrt
        
        password = ""
        
        while(1):
            
            char = msvcrt.getch().decode("utf-8") # legge il carattere inserito sulla tastiera (come una stringa di byte)

            # 1) L'utente preme invio
            if char == "\r": # se l'utente preme il tasto invio 
                
                print("")  # Stampa un newline alla fine dell'input
                return password
            
            # 2) L'utente preme il "backspace"
            elif char == "\b": # controlla se il carattere inserito è il "backspace"
                
                if password: # password (l'input dell'utente diventa)
                    
                    password = password[:-1] # Elimina l'ultimo carattere inserito
                    
                    print("\b \b", end="", flush=True)
                    
            # 3) L'utente preme un carattere stampabile, 
            elif char.isprintable(): # controlla se il carattere inserito corrisponde a un carattere stampabile se si
                
                password += char # Aggiunge il carattere alla password e stampa un asterisco sul terimnale
                
                print("*", end="", flush=True)
                
                # end = viene utilizzato per controllare il modo in cui la funzione print() gestisce la fine della striga, se è vuoto significa che non verrrà inserito nessun carattere alla fine della stringa
                
                # flusch = chiede esplicitamente al sistema di svuotare il buffer di output, in modo da garantire che la stringa di output venga immediatamente visualizzata a schermo
        
        
            # alla fine del cilo avremo la password,e quando l'utente premerà invio gli ritornerà la password
            
    
    else: # per Linux e macOS

        import tty, termios # permettono di impostaare la tasteira in modalità "raw" 

        fd = sys.stdin.fileno() 
        old_settings = termios.tcgetattr(fd) 

        try:
            tty.setraw(fd)
            password = ""

            while True:
                char = sys.stdin.read(1)
                if char == '\r' or char == '\n':
                    print('')
                    break

                else:
                    password += char
                    print('*', end='', flush=True)

            return password
        
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


# CRYPTO PSWD WHIT KEY

"""  
3 Funzione 

1) Genera la chiave casuale

2) Crypta la password e salvi la password cryptata all'interno di un file 
    i parameteri della funzione saranno la password da cryptare (data dall'utente)
    ritorno --> password cryptata

3) Decrypta la password, ovvero prende la password dal file, la legge e la decrypta
    i parametri in ingresso saranno la password cryptata e la chiave 
    ritorno --> password decryptata


4) Creare  un file main che: 
    1) l'utetne da una password
    2) crypti la password 
    3) la salvi nel file
    
    quando l'utente rientrera nel main gli verrà chiesta la password
    
    1) gli viene chiesta la password tramite input
    2) procedura che decrypti la password (leggendola dal file)
    
    3) se la password dell'utente corrisponde alla password decryptata può entrare altrimenti no
    
"""

from cryptography.fernet import Fernet
import os
import FUNZIONI.CreazioneCartelle as creazioneCartelle

privateKey = creazioneCartelle.GetPercorsoKey() + "/key.data"

def CasualKey(): # generazione e salvataggio chiave casuale 
    
    key = Fernet.generate_key()
    
    with open(privateKey, "wb") as file:
        file.write(key)
    
    return key

def save_key(): # lettura chiave
    
    if os.path.exists(privateKey):
        
        with open (privateKey, "rb") as file:
            key = file.read()
        return key
    else:
        
        key = CasualKey()
        
    return key

key = save_key()

def CryptPassword(password, filePath):
    
    fernet = Fernet(key)
    
    encrypted_password = fernet.encrypt(password.encode()) # encode() da str() --> bytes
    
    file = open(filePath, "wb") # wb = write bytes

    file.write(encrypted_password + b'\n') # scrive qui dentro la password cryptata e la salva in bytes
    file.close()
    
    return encrypted_password

def DecryptPassword(filePath):
    
    fernet = Fernet(key)
    
    file = open(filePath, "rb") # rb = read byteas 
    
    pswd_crypt = file.read().rstrip(b'\r \n') # prende la password cryptata .rstrip() tolgie l'utlimo carattere di newline per evitare errore iInvalidToken
    file.close()
    
    decrypted_pswd = fernet.decrypt(bytes(pswd_crypt)).decode() # da bytes --> str() = "matteorenzi1105"
    
    return decrypted_pswd # return str()
