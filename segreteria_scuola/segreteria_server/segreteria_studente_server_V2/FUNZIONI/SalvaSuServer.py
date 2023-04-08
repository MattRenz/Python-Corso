

import LIBRERIE_v2.httpclient as client


def SalvaStudentiSuServer(csStudente):
    
    contenuto = csStudente.CreaDatiStudenteSulServer()

    indirizzoIP = input("Indirizzo IP: ")
    porta = int(input("Porta: "))

    myHttp = client.MyHttpClient(indirizzoIP, porta)
    
    return myHttp.SendHTTPData("/CreaStudente", contenuto)


