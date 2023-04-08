#CREAZIONE DIZIONARIO 
codici = []

for x in range(400, 427):
    codici.append(chr(x))
    
lettere = []

for n in range(65, 91):
    lettere.append(chr(n))
    
diz = {}

for idx, c in enumerate(lettere):
    diz[c] = codici[idx]

diz[" "] = " "

print(diz)

frase = input(" ").upper()

cript = ""

for lettere in frase: #prendi solo le letteri che sooìno presenti nella frase e che sono presenti nel dizionario
    cript += str(diz[lettere]) + " " # aggiungi a "cript" il ripsettivo valore della chiave, (c: 28)
    # finito il ciclo dentro cript ci saranno tutti i vaòlori (numeri) corrispettivi alla nostra frase 
    
print(cript)


