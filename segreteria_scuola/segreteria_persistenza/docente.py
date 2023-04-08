import persona

class docente(persona.persona):

    def __init__(self, nome, cognome, identificativo, mail, listaCorsiInsegnati = None):
        super().__init__(nome, cognome, mail)

        self.__identificativo = identificativo
        self.__nome = nome
        self.__cognome = cognome
        self.__mail = mail
        
        if listaCorsiInsegnati == None:
            self.__listaCorsiInsegnati = []
        else:
            self.__listaCorsiInsegnati = listaCorsiInsegnati


    def AggiungiCorso(self, corso):
        self.__listaCorsiInsegnati.append(corso)

    def CreaDatiDocente(self):

        stringaDocente = f'{self.__nome};{self.__cognome};{self.__identificativo};{self.__mail};'

        for corsi in self.__listaCorsiInsegnati:
            
            stringaDocente = stringaDocente + str(corsi) + ";"

        return stringaDocente
    

    def CalcolaCorsi(self):

        print(f'\n Crosi insegnati da {self.__nome}: {len(self.__listaCorsiInsegnati)} \n Corsi: ')

        nmCorsi = 1
        
        for corso in self.__listaCorsiInsegnati:
            print(f' {nmCorsi}) {corso}')
            nmCorsi+=1
            
    def GetIdentificativo(self):

        return str(self.__identificativo)
    


