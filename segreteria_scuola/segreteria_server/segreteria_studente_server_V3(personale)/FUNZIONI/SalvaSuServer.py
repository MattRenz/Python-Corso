
import LIBRERIE_v3.httpclient as proc

def SalvaStudentiSuServer(csStudente):
    
    contenuto = csStudente.CreaDatiStudenteSulServer()

    IndirizzoIp = input("Indirizzo IP: ")
    porta = int(input("Porta: "))

    myHttp = proc.MyHttpClient(IndirizzoIp, porta)
    
    return myHttp.SendHTTPData("/CreaStudente", contenuto)



