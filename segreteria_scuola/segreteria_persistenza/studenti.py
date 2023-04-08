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


    def CreaDatiStudente(self):

        stringa = f'{self.__nome};{self.__cognome};{self.__mail};{self.__matricola};'

        for voti in self.___listaVoti:
            
            stringa = stringa + str(voti) + ";"
            
        return stringa
    
    
    def AggVoti(self, voto):
        
        self.___listaVoti.append(int(voto))
        
        
    def GetMatricola(self):

        return str(self.__matricola)
    

    def CalcolaMediaVoti(self):  # meetodo che calcola la media dei voti 
        
        iSomma = 0
        fMedia = 0
        
        for voto in self.___listaVoti:
            iSomma = iSomma + int(voto)
            
        fMedia = iSomma/len(self.___listaVoti)
        
        print("\n Il voto medio di " + self.__nome + " e' " + str(fMedia))
        
        return fMedia
    


