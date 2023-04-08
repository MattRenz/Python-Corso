

import LIBRERIA.httpclient as proc

def SalvaStudentiSuServer(csStudente):
    
    contenuto = csStudente.CreaDatiStudenteSulServer()

    indirizzoIp = input("Indirizzo IP: ")
    porta = int(input("Porta: "))

    myHttp = proc.MyHttpClient(indirizzoIp, porta)
    
    myHttp.SendHTTPData("/CreaStudente", contenuto)


