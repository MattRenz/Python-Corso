class Auto:
    
    def __init__(self, nome, marca, modello, velocita_max, anno):
        
        self.nome = nome
        self.marca = marca
        self.modello = modello
        self.velocita_max = velocita_max
        self.anno = anno
        
        velocita_max = int(velocita_max)
        
        
    def SchedaAuto(self):
        
        print("")
        return f"Scheda Auto\n Nome: {self.nome} \n Marca: {self.marca} \n Modello: {self.modello} \n Velocità Massima: {self.velocita_max} \n Anno: {self.anno}"
    
    def SuperCar(self):
        
        if self.velocita_max > 200:
            
            print("")
            return ("It's a Super Car")
        else: 
            return ("Non è una super car")
            
            
    def ControlloFreniEPasticche(self):
        
        if self.anno > 2006 and self.anno < 2014: 
            
            return("Controllo freni e pasticche ogni anno")
        
        if self.anno < 2006: 
            
            return("Attenzione usura freni e pasticche elevata controllo periodico")   

        if self.anno >= 2014 and self.anno <= 2020:
            
            return("Controllo freni e pasticche ongi 2 anni")
            
        if self.anno >= 2020 and self.anno <= 2023:
            
            return("Auto nuova stato usura basso")
            

Auto1 = Auto("Baby Black", "Porsche", "911 GT3 RS", 296, 2023)

Auto2 = Auto("Baby Dragon", "Porsche", "811 Spyder", 270, 2014)

Auto3 = Auto("Er Pandino", "Fiat", "Panda", 150, 2010)


print(Auto1.SchedaAuto())
print(f"{Auto1.nome} {Auto1.SuperCar()}")
print(f"Controllo Freni e Pasticche: {Auto1.ControlloFreniEPasticche()}")

print(Auto2.SchedaAuto())
print(f"{Auto2.nome} {Auto2.SuperCar()}")
print(f"Controllo Freni e Pasticche: {Auto2.ControlloFreniEPasticche()}")

print(Auto3.SchedaAuto())
print(f"{Auto3.nome} {Auto3.SuperCar()}")
print(f"Controllo Freni e Pasticche: {Auto3.ControlloFreniEPasticche()}")


        