import datetime

class veicoli:

    def __init__(self, modello, marca, numerotelaio, targa, cavalli, cambio, prezzo, anno, velocitaMax) -> None:

        self.__modello = modello
        self.__marca = marca
        self.__numeroTelaio = numerotelaio
        self.__traga = targa
        self.__cavalli = cavalli
        self.__cambio = cambio
        self.__prezzo = prezzo
        self.__anno = anno
        self.__velocitaMax = velocitaMax



    def SchedaPersonaleVeicolo(self):

        print(f'\n Scheda Personale: ')

        print(f'\n Marca: {self.__marca} \n Modello: {self.__modello} \n Anno: {self.__anno }\n Prezzo: {self.__prezzo}')

    def ShcedaDettagliata(self):

        print(f'\n Scheda Dettagliata')

        print(f'\n Marca: {self.__marca} \n Modello: {self.__modello} \n Anno: {self.__anno} \n Prezzo: {self.__prezzo} \n Numero Tealio: {self.__numeroTelaio} \n Cavalli: {self.__cavalli} \n Cambio: {self.__cambio} \n Targa: {self.__traga} \n Velocità Max: {self.__velocitaMax}')



    def CalcolaValoreVeicolo(self):

        today = datetime.date.today()

        ianno = today.year

        diffAnno = ianno - int(self.__anno) 

        self.__prezzo = int(self.__prezzo)

        PrezzoAuto = self.__prezzo


        print(f'\n Valore auto: {self.__modello} {self.__marca}')

        if diffAnno == 0:

            PrezzoAuto = self.__prezzo 

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {PrezzoAuto}€')

        elif diffAnno >= 1 and diffAnno < 2:

            PrezzoAuto1 = (self.__prezzo * 96) / 100
            ROundPrezzoAuto1 = round(PrezzoAuto1, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {ROundPrezzoAuto1}€')


        elif diffAnno >= 2 and diffAnno < 4:

            PrezzoAuto2 = (self.__prezzo * 90) / 100
            RoundPrezzoAuto2 = round(PrezzoAuto2, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto2}€')

        elif diffAnno >= 4 and diffAnno < 7: 

            PrezzoAuto4 = (self.__prezzo * 85) / 100
            RoundPrezzoAuto4 = round(PrezzoAuto4, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto4}€')


        elif diffAnno >= 7 and diffAnno < 12:

            PrezzoAuto7 = (self.__prezzo * 80) / 100
            RoundPrezzoAuto7 = round(PrezzoAuto7, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto7}€')

        elif diffAnno >= 12 and diffAnno < 17: 

            PrezzoAuto12 = (self.__prezzo * 70) / 100
            RoundPrezzoAuto12 = round(PrezzoAuto12, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto12}€')

        elif diffAnno >= 17 and diffAnno < 23:
            
            PrezzoAuto17 = (self.__prezzo * 50) / 100
            RoundPrezzoAuto17 = round(PrezzoAuto17, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto17}€')

        elif diffAnno >= 23 and diffAnno < 28:

            PrezzoAuto23 = (self.__prezzo * 30) / 100
            RoundPrezzoAuto23 = round(PrezzoAuto23, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto23}€')

        elif diffAnno >= 28 and diffAnno < 30:

            PrezzoAuto28 = (self.__prezzo * 20) / 100
            RoundPrezzoAuto28 = round(PrezzoAuto28, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto28}€')

        elif diffAnno > 30:

            PrezzoAuto = (self.__prezzo * 10) / 100
            RoundPrezzoAuto29 = round(RoundPrezzoAuto29, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto29}€')








        