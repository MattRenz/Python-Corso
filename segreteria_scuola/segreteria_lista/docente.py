""" 
Creare classe docente, attributi: Nome, Cognome, Idetnificativo, Lista Corsi insegnati. Con vari metodi calcola corsi insegnati

Con metodi inserisci docente, inserisci corso, calcola corsi insegnati
"""

import persona

class docente(persona.persona):

    profilo = "docente" 

    def __init__(self, nome, cognome, identificativo, mail):
        super().__init__(nome, cognome, mail)

        self.__identificativo = identificativo

        self.__nome = nome

        self.__listaCorsiInsegnati = []


    def MostraDocente(self):
        self.StampaScehdaPersona()
        print(f'\n Identificativo: {self.__identificativo}')

    def AggiungiCorso(self, corso):
        self.__listaCorsiInsegnati.append(corso)
    
    def CalcolaCorsi(self):

        print(f'\n Crosi insegnati da {self.__nome}: {len(self.__listaCorsiInsegnati)} \n Corsi: ')

        for corso in self.__listaCorsiInsegnati:

            print(f'{corso}')

    def GetIdentificativo(self):

        return self.__identificativo

    def GetCorsi(self):

        return self.__listaCorsiInsegnati



