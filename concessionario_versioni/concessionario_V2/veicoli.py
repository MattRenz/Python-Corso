import datetime

class veicoli:

    def __init__(self, modello, marca, numerotelaio, targa, annoUscita, prezzoListino):

        self.__modello = modello
        self.__marca = marca
        self.__numeroTelaio = numerotelaio
        self.__targa = targa
        self.__annoUscita = int(annoUscita)
        self.__prezzoListino = int(prezzoListino)
        
        self.__listaTarge = []
    
    def ScehdaVeicolo(self):

        print(f'\n Marca: {self.__modello} \n Modello: {self.__marca} \n Numero telaio: {self.__numeroTelaio} \n Targa: {self.__targa} \n Anno di uscita: {self.__annoUscita} \n Prezzo Listino: {self.__prezzoListino} €')

    def AggTarga(self, targa):
        
        self.__listaTarge.append(targa)

    def CalcolaValoreVeicolo(self):

        today = datetime.date.today()

        ianno = today.year

        diffAnno = ianno - int(self.__annoUscita) 

        self.__prezzoListino = int(self.__prezzoListino)

        PrezzoAuto = self.__prezzoListino

        print(f'\n Valore auto: {self.__marca} {self.__modello}')

        if diffAnno == 0:

            PrezzoAuto = self.__prezzoListino 

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {PrezzoAuto}€')

        elif diffAnno < 0:

            print("Errore, ricontrollare bene l'anno di uscita dell'Auto" + f'{self.__annoUscita} non valido')

        elif diffAnno == 1:

            PrezzoAuto1 = (self.__prezzoListino * 96) / 100
            ROundPrezzoAuto1 = round(PrezzoAuto1, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {ROundPrezzoAuto1}€')
            
        elif diffAnno >= 2 and diffAnno < 4:

            PrezzoAuto2 = (self.__prezzoListino * 90) / 100
            RoundPrezzoAuto2 = round(PrezzoAuto2, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto2}€')

        elif diffAnno >= 4 and diffAnno < 7: 

            PrezzoAuto4 = (self.__prezzoListino * 85) / 100
            RoundPrezzoAuto4 = round(PrezzoAuto4, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto4}€')

        elif diffAnno >= 7 and diffAnno < 12:

            PrezzoAuto7 = (self.__prezzoListino * 80) / 100
            RoundPrezzoAuto7 = round(PrezzoAuto7, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto7}€')

        elif diffAnno >= 12 and diffAnno < 17: 

            PrezzoAuto12 = (self.__prezzoListino * 70) / 100
            RoundPrezzoAuto12 = round(PrezzoAuto12, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto12}€')

        elif diffAnno >= 17 and diffAnno < 23:
            
            PrezzoAuto17 = (self.__prezzoListino * 50) / 100
            RoundPrezzoAuto17 = round(PrezzoAuto17, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto17}€')

        elif diffAnno >= 23 and diffAnno < 28:

            PrezzoAuto23 = (self.__prezzoListino * 30) / 100
            RoundPrezzoAuto23 = round(PrezzoAuto23, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto23}€')

        elif diffAnno >= 28 and diffAnno < 30:

            PrezzoAuto28 = (self.__prezzoListino * 20) / 100
            RoundPrezzoAuto28 = round(PrezzoAuto28, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto28}€')

        elif diffAnno > 30:

            PrezzoAuto = (self.__prezzoListino * 10) / 100
            RoundPrezzoAuto29 = round(RoundPrezzoAuto29, 2)

            print(f'La tua auto/moto ha: {diffAnno} anni')
            print(f'\n Valutata: {RoundPrezzoAuto29}€')









        