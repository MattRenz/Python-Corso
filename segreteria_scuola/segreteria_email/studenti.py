import persona as proc

DBpasswordUtente = ""

class Studente(proc.persona):

    def __init__(self, nome, cognome, matricola, mail, listaVoti = None):
        super().__init__(nome, cognome, mail)

        self.__matricola = matricola
        self.__nome = nome
        self.__cognome = cognome
        self.__mail = mail


        if listaVoti == None:

            self.___listaVoti = []
        else:
            self.___listaVoti = listaVoti


    def GetListaVoti(self):
        return self.___listaVoti
    
    def GetName(self):
        
       return self.__nome
   
    def GetCognome(self):
        
        return self.__cognome
    
    def CreaDatiStudente(self):

        stringa = f'{self.__nome};{self.__cognome};{self.__mail};{self.__matricola};'

        for voti in self.___listaVoti:
            
            stringa = stringa + str(voti) + ";"
            
        return stringa
    
    def AggVoti(self, voto):
        
        self.___listaVoti.append(int(voto))
          
    def GetMatricola(self):

        return str(self.__matricola)
    
    def GetEmail(self):
        
        return self.__mail
    
    def CalcolaMediaVoti(self):  # metodo che calcola la media dei voti 
        try:
            iSomma = 0
            fMedia = 0
            
            for voto in self.___listaVoti:
                iSomma = iSomma + int(voto)
            
            fMedia = iSomma/len(self.___listaVoti)
            
        except:
            print(f'\n {self.__nome} {self.__cognome} Non ha voti')
            
        finally:
            
            print("\n Il voto medio di " + self.__nome + " e' " + str(fMedia))
        
        return fMedia
    
    
    