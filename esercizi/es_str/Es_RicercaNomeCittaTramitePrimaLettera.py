import FUNZIONI.Funzione_RicercaNomeCittaTramitePrimaLettera as proc

Carattere = input("Prima lettera della città che si cerca: ")

TrovaCitta = proc.RicercaNomeCittaTramitePrimaLettera(["Roma", "Firenze", "Ragusa", "Milano"], Carattere)

print(TrovaCitta)