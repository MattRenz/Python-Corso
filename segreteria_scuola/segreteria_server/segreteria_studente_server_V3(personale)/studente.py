import persona as proc

class Studente(proc.persona):

    def __init__(self, nome, cognome, mail, matricola, listaVoti = None):
        super().__init__(nome, cognome, mail)

        self.__matricola = matricola
        self.__nome = nome
        self.__cognome = cognome
        self.__mail = mail


        if listaVoti == None:

            self.___listaVoti = []
        else:
            self.___listaVoti = listaVoti


    def AggVoti(self, voto):
        
        self.___listaVoti.append(int(voto))

    def stampaScheda(self):
        
        print(f'\nNome: {self.__nome}\nCognome: {self.__cognome}\nEmail:{self.__mail}\nMaatricola:{self.__matricola}')

    def CreaDatiStudenteSulServer(self):

        nome = str(self.__nome).replace(" ", "+")
        cognome = str(self.__cognome).replace(" ", "+")

        stringa = "Nome="+nome+ "&" + "Cognome="+ cognome + "&" + "Email=" + self.__mail + "&" + "Matricola=" + self.__matricola

        if len(self.___listaVoti) > 0:

            listaVoti = ""

            for voto in self.___listaVoti:

                listaVoti = listaVoti + str(voto) + ";"

            stringa = stringa + "&" + "Voti=" + listaVoti
            
        return stringa
    
    def GetMatricola(self):
        
        return self.__matricola


    # def CalcolaMediaVoti(self):  # metodo che calcola la media dei voti 
    #     try:
    #         iSomma = 0
    #         fMedia = 0
            
    #         for voto in self.___listaVoti:
    #             iSomma = iSomma + int(voto)
            
    #         fMedia = iSomma/len(self.___listaVoti)
            
    #     except:
    #         print(f'\n {self.__nome} {self.__cognome} Non ha voti')
            
    #     finally:
            
    #         print("\n Il voto medio di " + self.__nome + " e' " + str(fMedia))
        
    #     return fMedia
    
    
    