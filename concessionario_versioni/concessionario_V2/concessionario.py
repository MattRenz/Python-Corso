import os
import sys
import automobili
import automobili_usate

print("\n Inserire il path di dove si vouole salvare le proprie auto")

pathLinuxAutoNuove = input("Path auto nuove : ")
# \\concessionario_versioni\\concessionario_V2\\DB_Auto_nuove
pathLinuxAutoUsate = input("Path auto usate: ")
# \\concessionario_versioni\\concessionario_V2\\DB_Auto_usate

# FUNZIONI AUTO NUOVE
def SalvaAuto(nuovaAuto):

    sNomeFile = pathLinuxAutoNuove + "/" + nuovaAuto.GetTarga().upper() + ".csv"

    
    sContenutoFile = automobili.automobili.ContenutoFile(nuovaAuto)

    file = open(sNomeFile, "w")
    file.write(sContenutoFile)
    file.close()

def GetCarburante(currfile, carburanteUser):

    listaCarburantiAuto = []
   
    sNomeFile = pathLinuxAutoNuove + "/" + currfile 
    file = open(sNomeFile, "r")
    contenutoFile = file.readline()
    file.close()
    
    contenutoFileSplit = contenutoFile.split(";")
    
    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
        
    marca = contenutoFileSplit[1]
    modello = contenutoFileSplit[0]  
    carburante = contenutoFileSplit[9]
    numTelaio = contenutoFileSplit[2]
    
    if carburanteUser.lower() == carburante.lower():
        
        s = f'\n Nm. Telaio:{numTelaio} / {marca} {modello} = {carburante}'
        
        listaCarburantiAuto.append(s)

    return listaCarburantiAuto

def GetTargaAuto(currfile):
    
    listaTargeAuto = []
    
    sNomeFile = pathLinuxAutoNuove + "/" + currfile 
    
    file = open(sNomeFile, "r")
    contenutoFile = file.readline()
    file.close()
    
    contenutoFileSplit = contenutoFile.split(";")
    
    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
        
    targa = contenutoFileSplit[3] 
    marca = contenutoFileSplit[1]
    modello = contenutoFileSplit[0]
    stringa = f'{targa[0:2]}-{targa[2:5]}-{targa[5:7]} = {marca} {modello}'

    listaTargeAuto.append(stringa)
    return listaTargeAuto    

def LeggiAuto(currfile):
    
    sNomeFile = pathLinuxAutoNuove + "/" + currfile
    
    file = open(sNomeFile, "r")
    contenutoFile = file.readline()
    file.close()
    
    contenutoFileSplit = contenutoFile.split(";")
    
    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
    
    modello = contenutoFileSplit[0]
    marca = contenutoFileSplit[1]
    numeroTelaio = contenutoFileSplit[2]
    targa = contenutoFileSplit[3]
    annoUscita = contenutoFileSplit[4]
    prezzoListino = contenutoFileSplit[5]
    garanzia = contenutoFileSplit[6]
    bagagliaio = contenutoFileSplit[7]
    cerchi = contenutoFileSplit[8]
    carburante = contenutoFileSplit[9]
    
    listaOptional = []

    if len(contenutoFileSplit) > 10:
        
        for optional in contenutoFileSplit[10:]:
            listaOptional.append(optional)
            csOptional = automobili.automobili(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino, garanzia, bagagliaio, cerchi, carburante, listaOptional)
    else:
        csOptional = automobili.automobili(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino, garanzia, bagagliaio, cerchi, carburante)    
        
    return csOptional
    
    
# FUNZIONI AUTO USATE
def SalvaAutoUsate(nuovaAutoUsata):
    
    nomefile = pathLinuxAutoUsate + "/" + nuovaAutoUsata.GetTargaAutoUsata().upper() + ".csv"
    
    stringaFile = automobili_usate.automobiliUsate.ContenutoFileAutoUsata(nuovaAutoUsata)
    
    file = open(nomefile, "w")
    file.write(stringaFile)
    file.close()
  
def GetCarburanteAutoUsate(currfile, carburanteUser):
    
    listaCarburantiAutoUsate = []
   
    sNomeFile = pathLinuxAutoUsate + "/" + currfile 
    file = open(sNomeFile, "r")
    contenutoFile = file.readline()
    file.close() 
    
    contenutoFileSplit = contenutoFile.split(";")

    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
        

    marca = contenutoFileSplit[1]
    modello = contenutoFileSplit[0]
    carburante = contenutoFileSplit[8]
    numTelaio = contenutoFileSplit[2]


    if carburanteUser.lower() == carburante.lower():
        
        s = f'\n Nm. Telaio:{numTelaio} / {marca} {modello} = {carburante}'
        
        listaCarburantiAutoUsate.append(s)

    return listaCarburantiAutoUsate

def LeggiAutoUsata(currFile):
    
    nomefile = pathLinuxAutoUsate + "/" + currFile
    
    file = open(nomefile, "r")
    contenitofile = file.readline()
    file.close()
    
    contenutoFileSplit = contenitofile.split(";")
    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
        
    modello = contenutoFileSplit[0]
    marca = contenutoFileSplit[1]
    numeroTelaio = contenutoFileSplit[2]
    targa = contenutoFileSplit[3]
    annoUscita = contenutoFileSplit[4]
    prezzoListino = contenutoFileSplit[5]
    bagagliaio = contenutoFileSplit[6]
    cerchi = contenutoFileSplit[7]
    carburante = contenutoFileSplit[8]
    nmKM = contenutoFileSplit[9]
    condizioni = contenutoFileSplit[10]
    
    listaOptional = []
    
    if len(contenutoFileSplit) > 11:
        
        for optional in contenutoFileSplit[11:]:
            listaOptional.append(optional)
            nuovaAuto_Usata = automobili_usate.automobiliUsate(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino,bagagliaio, cerchi, carburante, nmKM, condizioni, listaOptional)
    else: 
        nuovaAuto_Usata = automobili_usate.automobiliUsate(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino, bagagliaio, cerchi, carburante, nmKM, condizioni)
        
    return nuovaAuto_Usata

def GetTargaAutoUsata(currfile):
    
    listaTargeAutosate = []

    nomefile = pathLinuxAutoUsate + "/" + currfile
    
    file = open(nomefile, "r")
    contenutoFile = file.readline()
    file.close()
    
    contenutoFileSplit = contenutoFile.split(";")
    if contenutoFileSplit[len(contenutoFileSplit) -1] == '': 
        contenutoFileSplit = contenutoFileSplit[0:len(contenutoFileSplit)-1]
    
    targa = contenutoFileSplit[3] 
    marca = contenutoFileSplit[1]
    modello = contenutoFileSplit[0]
    stringa = f'{targa[0:2]}-{targa[2:5]}-{targa[5:7]} = {marca} {modello}'

    listaTargeAutosate.append(stringa)
    return listaTargeAutosate  

print("")
print("Concessionario".center(80, "_"))


while(1):
       
    Oper003 = input("\n (1 Auto nuova 2 Auto usata)")
                
    # AUTO NUOVE
    if Oper003 == "1":
        print("\n Sezione auto nuove")
        
        while(1): 
            Oper001 = input("\n (1 Procedure, 2 Archivi, 3 esci)")
            
            if Oper001 == "3":
                sys.exit()
                
            # SEZIONE PROCEDURE AUTO NUOVE
            if Oper001 == "1":
                print("\n Procedure")
            
                while(1):
                    OperAuto = input(f'\n (1 Inserisci Auto, 2 Aggiungi Optional, 3 Rimuovi Optional, 4 Stampa Valore Auto, 5 esci)')
                    
                   
                    if OperAuto == "5":
                        sys.exit()

                    # INSERIMENTO AUTO NUOVA
                    if OperAuto == "1":
            
                        print("\n Inserimento AUTO NUOVA")

                
                        modello = input("\n Modello: ")
                        marca = input("Marca: ")
                        numeroTelaio = input("Numero Telaio: ").upper()
                        targa = input("Targa: ").upper()
                        annoUscita = int(input("Anno uscita: "))
                        prezzoListino = int(input("Prezzo listino: "))
                        garanzia = input("Garanzia: ")
                        bagagliaio = input("Bagliaio: ")
                        cerchi = input("Cerchi: ")
                        carburante = input("Carburante: ")

                        nuovaAuto = automobili.automobili(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino,garanzia,bagagliaio,cerchi,carburante)
                        nuovaAuto.AggCarburante(carburante)
                        SalvaAuto(nuovaAuto)
                        
                        
                    # AGGIUNGI OPTIONAL
                    if OperAuto == "2":

                        print("\n Inserire la targa dell'auto per aggiungere optional")
                        
                        targaAuto = input("\n Targa: ").upper()
                        optional = input("\n Optional: ")
                        
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        trovaTarga = 0
                        for targa in listaFile:
                            
                            if targa == targaAuto + ".csv":
                                nuovaAuto = LeggiAuto(targa)
                                nuovaAuto.AggOptional(optional)
                                SalvaAuto(nuovaAuto)
                                trovaTarga = 1
                                
                        if trovaTarga == 0:
                            print("\n Targa non trovata")
                        else: 
                            print("\n Optional aggiunto correttamente")

                    # RIMUOVI OPTIONAL
                    if OperAuto == "3":
                        
                        print("\n Inserie Targa e optional da rimuove dell'auto")
                        
                        targaUserRemove = input("\n Targa: ").upper()
                        
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        OptionalRemove = 0
                        for targa in listaFile:
                            if targa == targaUserRemove + ".csv":
                                nuovaAuto = LeggiAuto(targa)
                                nuovaAuto.TrovaOptional()
                                
                                optionalRemove = input("\n Optional remove: ").lower()
                                nuovaAuto.RimuoviOptional(optionalRemove)
                                SalvaAuto(nuovaAuto)
                                   
                        if targaUserRemove == 0:
                            print("\n Targa non trovata")       
        
                    # CALCOLA VALORE AUTO   
                    if OperAuto == "4":
                                            
                        targaUser = input("Targa: ").upper()
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        
                        trovaTargaValore = 0
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        for targa in listaFile:
                    
                            if targa == targaUser + ".csv":
                                nuovaAuto = LeggiAuto(targa)
                                nuovaAuto.CalcolaValoreVeicolo()
                                trovaTargaValore = 1
                                
                        if trovaTargaValore == 0:
                            print("\n Targa non trovata")
                                         
            # SEZIONE ARCHIVI AUTO NUOVE   
            if Oper001 == "2":
                print("\n Sezione Archivi")
                while(1):
                    Oper002 = input("\n (1 Stampa Shcheda Auto (auto), 2 Stampa optional (auto), 3 Trova targhe (all), 4 Trova Auto da carburante)")
                    
                    # STAMPA SCHEDA
                    if Oper002 == "1":
                        
                        print(f'\n Scheda Auto')
                        targaUser = input("\n Inserie la targa dell'auto: ").upper()
                        
                        trovaTargaAuto = 0
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        for targa in listaFile:
                            
                            if targa == targaUser + ".csv": 
                                trovaTargaAuto = 1
                                nuovaAuto = LeggiAuto(targa)
                                nuovaAuto.ScehdaAuto()  
                                          
                        if trovaTargaAuto == 0:
                            print("Auto non trovata")
                            
                    # TROVA OPTIONAL
                    if Oper002 == "2":
                    
                        targaUser = input("\n Inserisci targa: ").upper()
                        
                        trovaTargaOptional = 0
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        for targa in listaFile:
                            
                            if targa == targaUser + ".csv":
                                trovaTargaOptional = 1
                                nuovaAuto = LeggiAuto(targa)
                                nuovaAuto.TrovaOptional()
                                            
                        if trovaTargaOptional == 0:
                            print("Targa non trovata")
                            
                    # TROVA TARGHE
                    if Oper002 == "3":

                        listaFile = os.listdir(pathLinuxAutoNuove)
                        for targa in listaFile:
                            nuovaAuto = GetTargaAuto(targa)
                            for i in nuovaAuto:
                                print(i)
                    
                    # TROVA CARBURANTE
                    if Oper002 == "4":
                        
                        listaFile = os.listdir(pathLinuxAutoNuove)
                        
                        carburanteUser = input("\n Tipo carburante: ").lower()
                            
                        for targa in listaFile:

                            nuovaAuto = GetCarburante(targa, carburanteUser)
                            for i in nuovaAuto:
                                print(i)


    
                             
                    
            

    # AUTO USATE 
    if Oper003 == "2":
        print("\n Sezione auto usate")
        
        while(1):
           Oper001 = input("\n (1 Procedure, 2 Archivi, 3 esci)") 
           
           if Oper001 == "3":
               sys.exit()
               
           # SEZIONE PROCEDURE 
           if Oper001 == "1":
                print("\n Procedure")
           
                OperAuto = input(f'\n (1 Inserisci Auto, 2 Aggiungi optional, 3 Rimuovi Optioanl, 4 Stampa valore auto usata, 5 esci)')
            
                if OperAuto == "5":
                    sys.exit()
                    
                # INSERIMENTO AUTO USATA
                if OperAuto == "1":
        
                    print("\n Inserimento  AUTO USATA")

                    modello = input("\n Modello: ")
                    marca = input("Marca: ")
                    numeroTelaio = input("Numero Telaio: ").upper()
                    targa = input("Targa: ").upper()
                    annoUscita = int(input("Anno uscita: "))
                    prezzoListino = int(input("Prezzo listino: "))
                    bagagliaio = input("Bagliaio: ")
                    cerchi = input("Cerchi: ")
                    carburante = input("Carburante: ")
                    nmKM = int(input("Chilometraggio: "))
                    print("\n Inserire le condizioni pessime, discrete, buone, ottime, nuova")
                    condizioni = input("\n Condizioni: ")
                    
                    nuovaAutoUsata = automobili_usate.automobiliUsate(modello,marca,numeroTelaio,targa,annoUscita,prezzoListino,bagagliaio,cerchi,carburante, nmKM, condizioni)
                    SalvaAutoUsate(nuovaAutoUsata)
                    nuovaAutoUsata.AggTarga(targa)
          
                # AGGIUNGI OPTIONAL
                if OperAuto == "2":
                    print("\n Inserisci optional")
                    
                    targaUser = input("\n Inserisci targa: ").upper()
                    optional = input("\n Optional: ")
                    
                    listaFileUsate = os.listdir(pathLinuxAutoUsate)
                    trovaTargaOptionalUsata = 0
                    for targa in listaFileUsate:
                        
                        if targa == targaUser + ".csv":
                            nuovaAutoUsata = LeggiAutoUsata(targa)
                            nuovaAutoUsata.AggOptionalAutoUsata(optional)
                            SalvaAutoUsate(nuovaAutoUsata)
                            trovaTargaOptionalUsata = 1
                            
                    if trovaTargaOptionalUsata == 0:
                        print("\n Targa non trovata")
                    else:
                        print("\n Optional aggiunto correttamente")
                            
                # RIMUOVI OPTONAL 
                if OperAuto == "3":

                    print("\n Inserie Targa e optional da rimuove dell'auto")
                    
                    targaUserRemove = input("\n Targa: ").upper()
                    
                    listaFileUsate = os.listdir(pathLinuxAutoUsate)

                    OptionalRemove = 0
                    for targa in listaFileUsate:
                        if targa == targaUserRemove + ".csv":
                            nuovaAutoUsata = LeggiAutoUsata(targa)
                            nuovaAutoUsata.TrovaOptionalAutoUsata()
                            OptionalRemove = 1
                            optionalRemove = input("\n Optional remove: ").lower()
                            nuovaAutoUsata.RimuoviOptionalAutoUsata(optionalRemove)
                            SalvaAutoUsate(nuovaAutoUsata)

                                
                    if targaUserRemove == 0:
                        print("\n Targa non trovata")    

                # CALCOLA VALORE AUTO 
                if OperAuto == "4":
                    targaUser = input("\n Targa: ").upper()

                    listaFile = os.listdir(pathLinuxAutoUsate)
                    trovaTarga = 0

                    for targa in listaFile:
                        if targa == targaUser + ".csv":
                            nuovaAutoUsata = LeggiAutoUsata(targa)
                            nuovaAutoUsata.CalcolaValoreAutoUsate()   
                            trovaTarga = 1
                    
                    if trovaTarga == 0:
                        print("\n Targa non trovata")


           # SEZIONE ARCHVI 
           if Oper001 == "2":
               
                print("\n Sezione Archivi")
                while(1):

                    Oper002 = input("\n (1 Stampa Shcheda Auto (auto), 2 Stampa optional (auto), 3 Trova targhe (all), 4 Trova Auto da carburante 5 Esci)")
                    
                    if Oper002 == "5":
                        sys,exit()

                    # STAMPA SCHEDA
                    if Oper002 == "1":
                        
                        print(f'\n Scheda Auto')
                        targaUser = input("\n Inserie la targa dell'auto: ").upper()
                        
                        trovaTargaAuto = 0
                        listaFile = os.listdir(pathLinuxAutoUsate)
                        for targa in listaFile:
                            
                            if targa == targaUser + ".csv": 
                                trovaTargaAuto = 1
                                nuovaAutoUsata = LeggiAutoUsata(targa)
                                nuovaAutoUsata.SchedaAutoUsata()  
                                          
                        if trovaTargaAuto == 0:
                            print("Auto non trovata")

                    # TROVA OPTIONAL
                    if Oper002 == "2":

                        targaUser = input("\n Inserisci targa: ").upper()
                        
                        trovaTargaOptional = 0
                        listaFile = os.listdir(pathLinuxAutoUsate)
                        for targa in listaFile:
                            
                            if targa == targaUser + ".csv":
                                trovaTargaOptional = 1
                                nuovaAutoUsata = LeggiAutoUsata(targa)
                                nuovaAutoUsata.TrovaOptionalAutoUsata()
                                            
                        if trovaTargaOptional == 0:
                            print("Targa non trovata")
                            
                
    
                    # TROVA TARGHE
                    if Oper002 == "3":

                        listaFile = os.listdir(pathLinuxAutoUsate)
                        for targa in listaFile:
                            nuovaAutoUsata = GetTargaAutoUsata(targa)
                            for i in nuovaAutoUsata:
                                print(i)
 
                    # TROVA CARBURANTE
                    if Oper002 == "4":
                        
                        listaFile = os.listdir(pathLinuxAutoUsate)
        
                        carburanteUser = input("\n Tipo carburante: ").lower()
                            
                        for targa in listaFile:

                            nuovaAutoUsate = GetCarburanteAutoUsate(targa, carburanteUser)
                            for i in nuovaAutoUsate:
                                print(i)
