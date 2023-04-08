import json

print("\n Inserire il path della cartella dove è salvato almeno un file in formato JSON per leggerlo. \n(è gia presente una cartella con all'interno dei file JSON)")
pathFile = input("\n Path: ")


with open(pathFile, "r") as file:
    
    file_Azienda = json.load(file)
    
    print(file_Azienda)
    

# Possiamo leggere anche un singolo elemento di un file 

print("\n Dipendenti")
with open(pathFile, "r") as file:
    
    file_studente = json.load(file)
    
    print(file_studente["dipendenti"])

