""" 
Gestione ristorante, conservare i nomi e i costi dei piatti dentro dei dizionari.
Dividere tra primi e secondi 
Stilare fatturato dei primi e fatturato dei secodni 
Stilare il fatturato di ogni piatto solamente se richiesto
Stilare il fatturato totale 

"""

def funzione(): 
    
    primi = {"Piatto1": "Cacio e pepe", "Piatto2": "Carbonara", "Piatto3": "Gricia"}
    costoPrimi = {"Piatto1": 8.50, "Piatto2": 10.00, "Piatto3": 9.50}
    secondi = {"Piatto1": "Filetto di manzo", "Piatto2": "Polpette al sugo", "Piatto3": "Fieltto di merluzzo"}
    costoSecondi = {"Piatto1": 11.00, "Piatto2": 7.50, "Piatto3": 9.00}
    
    print("Gestione risotrante".center(80, "_"))
    
    print("")
    
#portate   

    print("Primi".center(40,"_"))
    print("")
    portataPrimi_piatto1 = int(input(f'Portate di {primi["Piatto1"]}: '))
    portataPrimi_piatto2 = int(input(f'Portate di {primi["Piatto2"]}: '))
    portataPrimi_piatto3 = int(input(f'Portate di {primi["Piatto3"]}: '))
    print("")
    print("Secondi".center(40,"_"))
    print("")
    portataSeconda_piatto1 = int(input(f'Portate di {secondi["Piatto1"]}: '))
    portataSeconda_piatto2 = int(input(f'Portate di {secondi["Piatto2"]}: '))
    portataSeconda_piatto3 = int(input(f'Portate di {secondi["Piatto3"]}: '))
    
    
#fatturati 

    fatturatoPrimi = (costoPrimi["Piatto1"] * portataPrimi_piatto1) + (costoPrimi["Piatto2"] * portataPrimi_piatto2) + (costoPrimi["Piatto3"] * portataPrimi_piatto3)
    fatturatoSecondi = (costoSecondi["Piatto1"] * portataSeconda_piatto1) + (costoSecondi["Piatto2"] * portataSeconda_piatto2) + (costoSecondi["Piatto3"] * portataSeconda_piatto3)
    
    print("Fatturati".center(80, "_"))
    print("")  
    
    print(f'Fatturato primi {fatturatoPrimi}€')
    print(f'Fatturato secondi {fatturatoSecondi}€')
    print("")
    
    richiesta = input("Stialare il fatturato di ogni piatto: ").lower()
    
    if richiesta.find("si") > -1:                   
        print("")
        print("Fatturato di ogni piatto".center(40, "_"))
        
        fatturatoPrimiP1 = costoPrimi["Piatto1"] * portataPrimi_piatto1
        fatturatoPrimiP2 = costoPrimi["Piatto2"] * portataPrimi_piatto2
        fatturatoPrimiP3 = costoPrimi["Piatto3"] * portataPrimi_piatto3
        
        fatturatoSecondiP1 = costoSecondi["Piatto1"] * portataSeconda_piatto1
        fatturatoSecondiP2 = costoSecondi["Piatto2"] * portataSeconda_piatto2
        fatturatoSecondiP3 = costoSecondi["Piatto3"] * portataSeconda_piatto3

        print("")
        print("Fatturato piatti singoli primi: ")
        print("")
        print(f'Fatturato {primi["Piatto1"]}: {fatturatoPrimiP1}€')
        print(f'Fatturato {primi["Piatto2"]}: {fatturatoPrimiP2}€')
        print(f'Fatturato {primi["Piatto3"]}: {fatturatoPrimiP3}€')     
        
        print("")
        print("Fatturato piatti singoli secondi: ")
        print("")
        print(f'Fatturato {secondi["Piatto1"]}: {fatturatoSecondiP1}€')
        print(f'Fatturato {secondi["Piatto2"]}: {fatturatoSecondiP2}€')
        print(f'Fatturato {secondi["Piatto3"]}: {fatturatoSecondiP3}€')   
        print("")
funzione()