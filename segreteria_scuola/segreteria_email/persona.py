class persona(): 

    def __init__(self, nome, cognome, mail):

        self.__nome = nome
        self.__cognome = cognome
        self.__mail = mail


    def StampaScehdaPersona(self):

        print(f'\n Scheda personale: \n Nome: {self.__nome} \n Cognome: {self.__cognome} \n Email: {self.__mail}')


    


        
