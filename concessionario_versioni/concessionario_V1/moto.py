import veicoli

class moto(veicoli.veicoli):

    def __init__(self, modello, marca, numerotelaio, targa, cavalli, cambio, prezzo, anno, velocitaMax) -> None:
        super().__init__(modello, marca, numerotelaio, targa, cavalli, cambio, prezzo, anno, velocitaMax)

        self.__traga = targa
        self.__numeroTelaio = numerotelaio

    

    def StampaScehdaMoto(self):

        self.SchedaPersonaleVeicolo()


    def StampaScehdaMotoDettagliata(self):

        self.ShcedaDettagliata()

    def GetTargaMoto(self):

        return self.__traga
    

    def GetTelaioMoto(self):

        return self.__numeroTelaio