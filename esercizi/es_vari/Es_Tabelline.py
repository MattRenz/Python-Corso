import random
import datetime


def funzione():

    """
        Programma che esegue delle moltiplicazioni all'intenro di una lista
        levandole se giuste e riproponendole se sbagliate, conteggiando le risposte gisute e sbagliate

        popolare la lista di una coppia di domande e rispsota
    """
        
    lista = []
    risposteGiuste = 0
    risposteSbagliate = 0
        
    for n1 in range(1,11):
        for n2 in range(1,11):
            lista.append((n1, n2))
                

    ms = datetime.datetime.now().timestamp()
        
        
    while len(lista) > 0:
        seleziona = random.randint(0, len(lista) -1)
        numeri = lista.pop(seleziona)
        
        print("")
        print(f'Quanto fa {numeri[0]} * {numeri[1]}')
        risultato = numeri[0] * numeri[1]
        print("")
        risposta = int(input("Risultato: "))
            
        if risposta != risultato: 
            print("Risultato sbagliato, riprova")
            lista.append(numeri)
                
    #conteggio risposte giuste
        if risposta == risultato:
            risposteGiuste += 1
        else: 
            risposteSbagliate += 1
                
    #resoconto moltiplicazioni    
    print("")
    print(f'hai eseguito {risposteGiuste} risposte giuste')
    print(f'hai eseguito {risposteSbagliate} risposte sbagliate')
    
            
    if len(lista) == 0:
            
        percentualiRisposteGiuste = (risposteGiuste / (risposteGiuste + risposteSbagliate)) * 100
        percentualiRisposteSbagliate = (risposteSbagliate / (risposteGiuste + risposteSbagliate)) * 100
            
        percentualiRisposteGiuste = round(percentualiRisposteGiuste)
        percentualiRisposteSbagliate = round(percentualiRisposteSbagliate)
        print("")   
        
        print(f'Percentuale risposte giuste: {percentualiRisposteGiuste}%')
        print(f'Percentuali risposte sbagliate: {percentualiRisposteSbagliate}%')
            
    if percentualiRisposteGiuste > 87:
        print("")
        print("Test superarto") 
    else:
        print("")
        print("Testo non superato")       
    
    dif = datetime.datetime.now().timestamp() - ms
    

        
funzione()
        