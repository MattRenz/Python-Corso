import veicoli

class automobili(veicoli.veicoli):
        
        def __init__(self, modello, marca, numerotelaio, targa, annoUscita, prezzoListino, garanzia, bagagliaio, cerchi, carburante, listaOptional = None, listaCarburanti = None):
            super().__init__(modello, marca, numerotelaio, targa, annoUscita, prezzoListino)
        
            self.__modello = modello
            self.__marca = marca
            self.__numeroTelaio = numerotelaio  
            self.__targa = targa
            self.__annoUscita = int(annoUscita)
            self.__prezzoListino = int(prezzoListino)
            self.__garanzia = garanzia
            self.__bagliaio = bagagliaio
            self.__cerchi = cerchi
            self.__carburante = carburante
            
            if listaCarburanti == None:
                self.__listaCarburanti = []
            else:
                self.__listaCarburanti = listaCarburanti
            
            if listaOptional == None:
                self.__listaOptional = []
            else:
                self.__listaOptional = listaOptional  
                
        
        
        
        def AggCarburante(self, carburante):
        
            self.__listaCarburanti.append(carburante)
                               
        def TrovaOptional(self):
        
            if len(self.__listaOptional) > 0:
                print("\n L'auto: " + f'{self.__marca} {self.__modello} ha questi optional: ')
                nmProcedure = 1
                    
                for optional in self.__listaOptional:
                    
                    print(f'\n {nmProcedure}) {optional}')
                    nmProcedure +=1
            elif len(self.__listaOptional) <= 0:
                print(f"\n l'auto " + f'{self.__marca} {self.__modello} non ha optional')
                   
        def GetTarga(self):
            return self.__targa
    
        def ContenutoFile(self):                                           
            stringa = f'{self.__modello};{self.__marca};{self.__numeroTelaio};{self.__targa};{self.__annoUscita};{self.__prezzoListino};{self.__garanzia};{self.__bagliaio};{self.__cerchi};{self.__carburante};'

            for optional in self.__listaOptional:
                stringa = stringa + optional + ";"
            return stringa
    
        def ScehdaAuto(self):
            self.ScehdaVeicolo()
            print(f'\n Garanzia {self.__garanzia} anni \n Bagagliaio: {self.__bagliaio} litri \n Cerchi: {self.__cerchi} \n Lista Optional: {self.__listaOptional} \n Carburante: {self.__carburante}')
            
        def AggOptional(self, optional):
            self.__listaOptional.append(optional)
            
        def RimuoviOptional(self, removeOptional):
            
            lungListaptional = len(self.__listaOptional) # 5
            
            for optional in self.__listaOptional:
                
                if optional.lower() == removeOptional.lower():
                    
                    self.__listaOptional.remove(optional) # lista = 4 
                    
            if len(self.__listaOptional) < lungListaptional:
                print("\n Optional tolto correttamente")
            elif len(self.__listaOptional) == lungListaptional:
                print("\n Optional non tolto riprovare")
                          

                    
                    
                    
            
                    

