import json

listadict = []
dictstudenti = {}

print("\n Inserire path dove andranno salvati i file in formato JSON")
path = input("\n Path: ") #\File_JSON\saveFile

par = 0

while par == 0:

    oper = input("Hai parametri da inserire (si,no): ").lower()

    if oper == "no":
        par = 1
    
    else:

        nome = input("Inserisci nome: ")
        cognome = input("Cognome: ")
        facolta = input("Facolta: ")
        
        dictstudenti = {}
        dictstudenti["nome"] = nome
        dictstudenti["cognome"] = cognome
        dictstudenti["facolta"] = facolta

        listadict.append(dictstudenti)


stringaJSON = json.dumps(listadict)

filePath = path + "/" + "file.json" 

with open(filePath, "w") as file:
    
    file.write(stringaJSON)

