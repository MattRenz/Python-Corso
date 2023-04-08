import veicoli

class automobiliUsate(veicoli.veicoli):
    
    def __init__(self, modello, marca, numerotelaio, targa, annoUscita, prezzoListino, bagagliaio, cerchi, carburante, nmKM, condizioni, listaOptional = None, listaCarburante = None):
        super().__init__(modello, marca, numerotelaio, targa, annoUscita, prezzoListino)
        
        self.__modello = modello
        self.__marca = marca
        self.__numeroTelaio = numerotelaio
        self.__targa = targa
        self.__annoUscita = int(annoUscita)
        self.__prezzoListino = int(prezzoListino)
        self.__bagagliaio = bagagliaio
        self.__cerchi = cerchi
        self.__carburante = carburante
        self.__nmKM = int(nmKM)  
        self.__condizioni = condizioni #0-2 Pessime / 3-5 Discrete / 6-7 Buone / 7-9 Ottime / 10 Come nuova
        
        if listaCarburante == None:
            self.__listaCarburante = []
        else:
            self.__listaCarburante = listaCarburante

        if listaOptional == None:
            self.__listaOptional = []
        else:
            self.__listaOptional = listaOptional   
            
    def AggCarburanteAutoUsata(self, carburante):
        self.__listaCarburante.append(carburante)

    def TrovaOptionalAutoUsata(self):

        if len(self.__listaOptional) > 0:
            print("\n L'auto " + f'{self.__marca} {self.__modello} ha questi Optional: ')

            nmProcedure = 1

            for optional in self.__listaOptional:
                print(f'\n {nmProcedure}) {optional}')
                nmProcedure += 1
        elif len(self.__listaOptional) <= 0:
            print("\n L'auto" + f'{self.__marca} {self.__modello} non ha optional')

    def GetTargaAutoUsata(self):
        return self.__targa

    def ContenutoFileAutoUsata(self):

        stringa = f'{self.__modello};{self.__marca};{self.__numeroTelaio};{self.__targa};{self.__annoUscita};{self.__prezzoListino};{self.__bagagliaio};{self.__cerchi};{self.__carburante};{self.__nmKM};{self.__condizioni};'
   
        for optional in self.__listaOptional:
        
            stringa = stringa + optional + ";"
        return stringa
    
    def SchedaAutoUsata(self):
        self.ScehdaVeicolo()
        
        print(f'\n Bagagliaio: {self.__bagagliaio} litri \n Cerchi: {self.__cerchi} \n Carburante: {self.__carburante} \n Numeri Km: {self.__nmKM} \n Condizione: {self.__condizioni} \n Lista Optional: {self.__listaOptional}')

    def  AggOptionalAutoUsata(self, optional):  
        self.__listaOptional.append(optional)
        
    def RimuoviOptionalAutoUsata(self, removeOptional):
             
        lungListaptional = len(self.__listaOptional) 
            
        for optional in self.__listaOptional:
                
            if optional.lower() == removeOptional.lower():
                    
                self.__listaOptional.remove(optional) 
                    
            if len(self.__listaOptional) < lungListaptional:
                print("\n Optional tolto correttamente")
            elif len(self.__listaOptional) == lungListaptional:
                print("\n Optional non tolto riprovare")


    def CalcolaValoreAutoUsate(self):


        daRottamare = (self.__prezzoListino * 10) / 100 # 2000.000 
        comeNuova = (self.__prezzoListino * 90) / 100 # 1.000 <
        
        svalutazioneBassa = (self.__prezzoListino * 86) / 100 # 1.000 - 3.000
        svalutazoneMedia_Basa = (self.__prezzoListino * 72) / 100 # 3.000 - 10.000
        svalutazionMedia00 = (self.__prezzoListino * 59) / 100 # 10.000 - 50.000
        svalutazioneMedia01 = (self.__prezzoListino * 50) / 100  # 50.000 - 75.000
        svalutazoneMedia_Alta = (self.__prezzoListino * 45) / 100 # 75.000 - 120.000
        svalutazioAlta00 = (self.__prezzoListino * 45) / 100 # 120.000 - 170.000
        savalutazionAlta01 = (self.__prezzoListino * 33) / 100 # 170.000 - 200.000
        
        #  1000 <
        if self.__nmKM > 0 and self.__nmKM <= 1000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Valore: {comeNuova}')


        # 220.000 >
        if self.__nmKM  > 220000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore attuale: {daRottamare}')

        # 1000Km - 3000
        if self.__nmKM > 1000 and self.__nmKM <= 3000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {svalutazioneBassa}')
    
        # 3.000 - 10.000
        if self.__nmKM > 3000 and self.__nmKM <= 10000:

            print("\n L'auto" + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino}  \n Valore: {svalutazoneMedia_Basa}')


        # 10.000 - 50.000
        if self.__nmKM > 10000 and self.__nmKM <= 50000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {svalutazionMedia00}')


        # 50.000 - 75.000
        if self.__nmKM > 50000 and self.__nmKM <= 75000:
            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {svalutazioneMedia01}')

        # 75.000 - 120.000
        if self.__nmKM > 75000 and self.__nmKM <= 120000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {svalutazoneMedia_Alta}')


        # 120.000 - 170.000
        if self.__nmKM > 120000 and self.__nmKM <= 170000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {svalutazioAlta00}')


        # 170.000 - 200.000
        if self.__nmKM > 170000 and self.__nmKM <= 200000:

            print("\n L'auto " + f'{self.__marca} {self.__modello} ha {self.__nmKM} di chilometraggio. Condizione auto: {self.__condizioni}')

            print(f'\n Perzzo listino: {self.__prezzoListino} \n Valore: {savalutazionAlta01}')

