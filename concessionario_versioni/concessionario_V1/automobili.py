import veicoli

class automobili(veicoli.veicoli):
        
        def __init__(self, modello, marca, numerotelaio, targa, cavalli, cambio, prezzo, anno, velocitaMax, numeroPorte, litriBagaglialio) -> None:
                super().__init__(modello, marca, numerotelaio, targa, cavalli, cambio, prezzo, anno, velocitaMax)

                self.__numeroPorte = numeroPorte
                self.__litriBagagliaio = litriBagaglialio
                self.__numeroTelaio = numerotelaio
                self.__traga = targa
    

        def StampaSchedaAuto(self):

            self.SchedaPersonaleVeicolo()


        def StampaSchedaAutoDettagliata(self):

            self.ShcedaDettagliata()

            print(f'\n Numero porte: {self.__numeroPorte}')
            
            print(f'\n Litri Bagagliaio: {self.__litriBagagliaio}')


        def GetTarga(self):

            return self.__traga
    
        def GetNumeroTelaio(self):

            return self.__numeroTelaio
