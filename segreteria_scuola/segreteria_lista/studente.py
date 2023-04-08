# Incapsulamento in Python

import persona 
import re

class studente(persona.persona):

    def __init__(self,nome,cognome,matricola, mail):
        super().__init__(nome, cognome, mail) # classe persona

        self.__mail = mail

        self.__nome = nome    
        
        self.__matricola = matricola
    
        self.__listaVotiEsame = [] # lista vuota dove aggiungiamo numeri
 

    def ControlloEmail(self):

        regex = r'\b[A-Z a-z 0-9._%+-]+@[A-Z a-z 0-9.-]+\.[A-Z|a-z]{2,7}\b'
       
        if (re.fullmatch(regex, self.__mail)):
           print("\n Valid Email".center(20, "_"))
        else: 
           print("Invalid Email".center(20, "_"))
    

    def MostraStudente(self):

        self.StampaScehdaPersona()

    def AggiungiVoto(self, iVoto): # metodo che aggiunge un attributo alla lista vuota creata precedentemente
        self.__listaVotiEsame.append(iVoto) 
        

    def CalcolaMediaVoti(self):  # meetodo che calcola la media dei voti 
        
        iSomma = 0
        fMedia = 0
        
        for voto in self.__listaVotiEsame:
            iSomma = iSomma + voto
            
        fMedia = iSomma/len(self.__listaVotiEsame)
        
        print("\n Il voto medio di " + self.__nome + " e' " + str(fMedia))

    def GetMatricola(self):

        return self.__matricola



    
