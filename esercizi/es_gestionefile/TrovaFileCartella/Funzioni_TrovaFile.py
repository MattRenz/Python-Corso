import sys
import os


# TROVA FILE TRAMITE ESTENZIONE: 
def CercaFilePerEstenione(sDir, sExt):
 
    outList = [] # listaa riempita con la directory
    
    outList2 = [] # lista con i file del estenzione che gli abbiamo fornito
    
    sExt = sExt.lower() # tutto in minuscolo
    
    outList = os.listdir(sDir) # prende le directory 
   

    for file in outList:  # esegue il l'eleemnto file dentro la directory che gli abbiamo passato noi
        
        file = file.lower()
        if file.endswith(sExt): # controlla se la parte finale è presente è presente nell'estenzione dell'utente
           outList2.append(file) # in caso la condizione è vera, aggiunge il file (con l'estenzione dell'utente) nella lista vuota che abbiamo creato pirma
    
    return outList2            


# TROVA FILE TRAMITE NOME:
def CercaFilePerNome(sDir, sNomeDaCercare):
    
    outlsitNome = []
    
    sNomeDaCercare = sNomeDaCercare.lower()
    
    filelist = os.listdir(sDir) # prende la directory che fornisce l'utetne 
    
    for file in filelist: # esegue il l'elemnto file dentro la directory che gli abbiamo passato noi (prende i file 1 per 1)
        
        file = file.lower() # ogni singolo file lo rende in minuscolo
        
        lista = file.split(".") # splitta, inserisce detro una lista il nome del file
        
        if len(lista) >= 1: # se la lunghezza della lista che ho splittato è maggiore di 1, quindi se quando splitto il nome del file, (indipindentemente se il nome del file o cartella ha 1 o più parole) 
            if lista[0].find(sNomeDaCercare) >= 0: # se la condizione di prima è vera allora entra in quest'altro if, In queasto If lui cerca se la prima lettera della parola del file (che ricordiamo file sono i file della directory che io gli ho fornito prima) la cerca facendo >= 0 perché se non è presente il find riporta -1. Quindi stando in un for, lui confronta tutte le lettere del file , con la parola che io ho fornito
                outlsitNome.append(file) #se l'if precedente è vero aggiunge il file alla lista vuota 
    
    return outlsitNome


# TROVA FILE PER ESTENZIONE, CON COREZZIONE DIRECTORY. VERSIONE WINDOWS (CODICE DI MICHEL)
def CercaFilePerEstenzioneCorrezioneDirectory(Dir, Exc, Ricerca):
    
    root = '/'

    outListFile = [] # Uscita di file

    Exc = Exc.lower() # estenzione che si sta cercando tutta in minuscolo

    Replace = Dir.replace("\\", "/") # Sostituiamo \ con / (a causa di un problema di VSC o Windows non riconosce il carattere '\' e quindi non può splittarlo)
    
    DirSplit = Replace.split("/") # Rimuoviamo / dalla directory 
    
    finalDir = [] # Il path finale

    lista = os.listdir(root) # Determiniamo la home

    for check in lista: # eseguiamo l'elemento check dentro la home
        
        checkl = check.lower()
        
        if checkl == DirSplit[1].lower():
            NewDirecotry = root + check
            
            finalDir.append(NewDirecotry)
            
    x = 1 # X sarà l'indice nel path inserito dall'utente per un successivo for

    while len(finalDir) < (len(DirSplit))-1: 

        anacart = ''.join(finalDir) # Finchè il path giusto non è un elemento in meno del path impostato dall'utente (che include la root), continua
       
        listav = os.listdir(anacart) # Anacart sarà il path finale unito in modo da usarlo come path ausiliario per il for delle cartelle nel path
        x += 1 # Aumentiamo di 1 x per controllare la cartella successiva nel path dell'utente e non analizzare la home
        
        for elemento in listav:
            
            elementol = elemento.lower()
            
            if elementol == DirSplit[x].lower():
                
                listcar = root + elemento
                finalDir.append(listcar)
                
    listafin = os.listdir(''.join(finalDir))
    
    Ricerca = Ricerca.lower()
    
    if Ricerca == "estenzione":
    
        for file in listafin:
            
            if file.endswith(Exc):
                
                outListFile.append(file)
        
        return outListFile
            
    if Ricerca == "nome":
    
        outListName = []
        
        for file in listafin:
            
            file = file.lower()
            
            lista = file.split(".")
            
            if len(lista) >= 1:
                
                if lista[0].find(Exc) >= 0:
                    outListName.append(file)
                    
        return outListName
                

# TROVA FILE IN TUTTE LE DIRECTORY ESTENZIONE
def TrovPerEstenzione(Percorso, Ricerca):
    
    outListFile = []

    for root, dirs, files in os.walk(Percorso): # esegue gli elementi root, dirs, files, all'interno del percorso. Con walk ci permette di aprire tutte le cartelle e sotto cartelle di un percorso
    
        # Testing
        '''
        print("")
        print(f'Stai cercando nella directory: {root}')
        print("")
        print(f'Sono prsenti {len(dirs)} cartelle')
        print("")
        print(f'Sono presenti {len(files)} files')
        '''
        
        for SingoloFile in files: # prendiamo ogni singolo file dalla lista dei file
            Ricerca = Ricerca.lower()        
            SingoloFile = SingoloFile.lower()
            
            if SingoloFile.endswith(Ricerca):  # se la parte finale del file corrisponde alla parte finale dell'utene 
                outListFile.append(SingoloFile) #aggiungilo alla lista vuota
    
    return outListFile


def TrovaPerNome(Percorso, Ricerca):
    
    outListNameFile = []
    
    for root, dirs, files, in os.walk(Percorso): # esegue lo stesso ciclo di prima
        
        
        Ricerca = Ricerca.lower()
            
        for Singolofile in files: # prende ogni singolo file
            
            Singolofile = Singolofile.lower()
            
            SingoloFileSplit = Singolofile.split(".") # lo splittiamo con (".") cosi rimangono solo le parole
        
            if len(SingoloFileSplit) >= 0: #se la grandezza della lista è maggiore o uguale a 0 (quindi se cè almeno 1 elemento) entra nell'istruzione
                
                if SingoloFileSplit[0].find(Ricerca) >= 0: #se dentro il file splittato eseguendo il cilo di ogni parola (con [0]) trovi (find) la parola che sto cercando io 
                        
                    outListNameFile.append(Singolofile) # aggiungila alla lista (la parola) dentro la mia lista vuota   
    
    
    return outListNameFile


def TrovaCartella(Percorso, Ricerca):
        
    outListNameDir = []
    
    Ricerca = Ricerca.lower()
    
    for root, dirs, files, in os.walk(Percorso):
    
        for SingoloElemento in dirs: 
            
            SingoloElemento = SingoloElemento.lower()
                
            DirSplit = SingoloElemento.split()

            if len(DirSplit) >= -1: 
                        
                for i in range(0, len(DirSplit)):
                                
                    if DirSplit[i].find(Ricerca) >= 0:
                        outListNameDir.append(SingoloElemento)
                        
    return outListNameDir
                    
          
def Exit(input1, input2, input3, input4):
    
    exit = "exit".lower()
    
    if input1 == exit or input2 == exit or input3 == exit or input4 == exit:
        return sys.exit()
        


        
        
    
    
      