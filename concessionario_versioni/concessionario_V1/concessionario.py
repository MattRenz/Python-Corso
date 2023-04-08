import sys
import moto
import automobili as auto


print("CONCESSIONARIO".center(80, "_"))

listaAuto = []
listaMoto = []



while(1):

    Oper00 = input(f'(1 Sezione Auto, 2 Sezione Moto 3 Exit)')
    
    if Oper00 == "3":
        sys.exit()

# SEZIONE AUTO

    if Oper00 == "1":

        while(1):

            Oper001 = input(f'\n (1 Inserisci Auto, 2 Stampa Scheda Auto, 3 Stampa Scheda dettagliata, 4 Stampa Valore Auto, 5 esci)')

            if Oper001 == "1":

                print("\n Inserimento nuova auto".center(20, "_"))
        
                modello = input("\n Modello: ")
                marca = input("Marca: ")
                numeroTelaio = input("Numero Telaio: ")
                targa = input("Targa: ").lower()
                cavalli = input("Cavalli: ")
                cambio = input("Cambio: ")
                prezzo = input("Prezzo: ")
                anno = input("Anno di uscita: ")
                velcoitaMax = input("Velocità Max: ")
                numeroPorte = input("Numero porte: ")
                litriBagalialio = input("Litri bagaglialio: ")

                nuovaAuto = auto.automobili(modello, marca, numeroTelaio, targa, cavalli, cambio, prezzo, anno, velcoitaMax, numeroPorte, litriBagalialio)

                listaAuto.append(nuovaAuto)

            if Oper001 == "2": 

                print(f'\n Stampa scheda auto, scelgiere auto tramite telaio')

                telaio = input("\n Inserisci telaio: ").lower()

                trovaTelaio = 0

                for auto in listaAuto:

                    if nuovaAuto.GetNumeroTelaio() == telaio:

                        nuovaAuto.StampaSchedaAuto()

                        trovaTelaio = 1

                if trovaTelaio == 0:

                    print("Telaio non trovato")


            if Oper001 == "3":

                print(f'\n Stampa scheda auto dettagliata , scelgiere auto tramite telaio')

            
                telaio = input("\n Inserisci telaio: ").lower()

                trovaTelaio = 0

                for auto in listaAuto:

                    if nuovaAuto.GetNumeroTelaio() == telaio:

                        nuovaAuto.StampaSchedaAutoDettagliata()

                        trovaTelaio = 1

                if trovaTelaio == 0:

                    print("Telaio non trovato")

            if Oper001 == "4":

                Oper002 = input(f'\n (1 Ricerca per targa, 2 Ricerca per numero telaio)')

                if Oper002 == "1":
                        
                    while(1):    
                        
                        trovaTarga = 0

                        targa = input("\n Inserisci targa: ").lower()

                        for auto in listaAuto:

                            if nuovaAuto.GetTarga() == targa:
                                
                                trovaTarga = 1

                                nuovaAuto.CalcolaValoreVeicolo()

                        if trovaTarga == 0:

                            print("Targa non trovata")


                if Oper002 == "2":
                        
                    while(1):    

                        telaio = input("\n Inserisci telaio: ").lower()

                        trovaTelaio = 0

                        for auto in listaAuto:

                            if nuovaAuto.GetNumeroTelaio() == telaio:

                                nuovaAuto.CalcolaValoreVeicolo()

                                trovaTelaio = 1

                        if trovaTelaio == 0:

                            print("Telaio non trovato")


            if Oper001 == "5":

                sys.exit()


# SEZIONE MOTO

    if Oper00 == "2":

        while(1):

            Oper001 = input(f'(1 Inserisci Moto, 2 Stampa Scheda Moto, 3 Stampa Scheda dettagliata, 4 Stampa valore veicolo, 5 esci)')


            if Oper001 == "1":

                print("Inserimento nuova moto".center(20, "_"))

                modello = input("Modello: ")
                marca = input("Marca: ")
                numeroTelaio = input("Numero Telaio: ")
                targa = input("Targa: ")
                cavalli = input("Cavalli: ")
                cambio = input("Cambio: ")
                prezzo = input("Prezzo: ")
                anno = input("Anno di uscita: ")
                velcoitaMax = input("Velocità Max: ")

                nuovaMoto = moto.moto(modello, marca, numeroTelaio, targa, cavalli, cambio, prezzo, anno, velcoitaMax)

                listaMoto.append(nuovaMoto)
                
                #nuovaMoto = moto.moto("BMW", "ZT50", "2345", "RT-456-TY", 270, "Automatico", 90000, 2019, 360)

            if Oper001 == "2":

                print(f'\n Stampa scheda moto, scelgiere auto tramite telaio')

            
                telaio = input("\n Inserisci telaio: ").lower()

                trovaTelaio = 0

                for moto in listaMoto:
                    
                    if nuovaMoto.GetTelaioMoto() == telaio:

                        nuovaMoto.StampaScehdaMoto()

                        trovaTelaio = 1
                
                if trovaTelaio == 0:

                    print("Telaio non trovato")

            
            if Oper001 == "3":

                    
                print(f'\n Stampa scheda moto dettagliata, scelgiere auto tramite telaio')

        
                telaio = input("\n Inserisci telaio: ").lower()

                trovaTelaio = 0

                for moto in listaMoto:

                    if nuovaMoto.GetTelaioMoto() == telaio:

                        nuovaMoto.StampaScehdaMotoDettagliata()

                        trovaTelaio = 1

                if trovaTelaio == 0:

                    print("Telaio non trovato")


            if Oper001 == "4":

                Oper002 = input(f'\n (1 Ricerca per targa, 2 Ricerca per numero telaio)')

                if Oper002 == "1":
                        
                    while(1):    
                        
                        trovaTarga = 0

                        targa = input("\n Inserisci targa: ").lower()

                        for moto in listaMoto:

                            if nuovaMoto.GetTargaMoto() == targa:
                                
                                trovaTarga = 1

                                nuovaMoto.CalcolaValoreVeicolo()

                        if trovaTarga == 0:

                            print("Targa non trovata")



                if Oper002 == "2":
                        
                    while(1):    

                        telaio = input("\n Inserisci telaio: ").lower()

                        trovaTelaio = 0

                        for moto in listaMoto:

                            if nuovaMoto.GetTelaioMoto() == telaio:

                                nuovaMoto.CalcolaValoreVeicolo()

                                trovaTelaio = 1

                        if trovaTelaio == 0:

                            print("Telaio non trovato")



            if Oper001 == "5":
                sys.exit()
    
