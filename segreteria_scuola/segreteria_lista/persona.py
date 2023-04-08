
class persona(): 

    def __init__(self, nome, cognome, mail):

        self.__nome = nome
        self.__cognome = cognome
        self.__mail = mail

        if mail.find("@")>= 0:

            self.__mail = mail
        else:
            self.__mail = "nd"
            print("Email errata")

    def StampaScehdaPersona(self):

        print(f'\n Scheda personale: \n Nome: {self.__nome} \n Cognome: {self.__cognome}')


    def SetMail(self, mail):

        self.__mail = mail


        
